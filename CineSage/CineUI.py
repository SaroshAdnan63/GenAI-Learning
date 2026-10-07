import html
import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel
from typing import List, Optional
from langchain_core.output_parsers import PydanticOutputParser
load_dotenv()
from langchain.chat_models import init_chat_model

# ---------------------------------------------------------------- page setup
st.set_page_config(page_title="CineScan · Movie Extractor", page_icon="🎬", layout="centered")


@st.cache_resource
def get_model():
    return init_chat_model("google_genai:gemini-3.6-flash")


model = get_model()


# ------------------------------------------------------------ your original
class Movie(BaseModel):
    title: str
    release_year: Optional[int]
    genre: List[str]
    director: Optional[str]
    cast: List[str]
    rating: Optional[float]
    summary: str


parser = PydanticOutputParser(pydantic_object=Movie)

prompt = ChatPromptTemplate.from_messages([
    ('system', """
 Extract the movie information from the paragraph
 {format_instructions} 
"""),
    ('human', "{paragraph}")
])

# ---------------------------------------------------------------------- CSS
st.markdown("""
<style>
.block-container {padding-top: 2rem; max-width: 820px;}

.hero {
    background: linear-gradient(135deg, #7F00FF 0%, #E100FF 50%, #FF512F 100%);
    border-radius: 22px;
    padding: 2.2rem 2rem;
    text-align: center;
    color: #fff;
    box-shadow: 0 12px 30px rgba(127, 0, 255, 0.25);
    margin-bottom: 1.6rem;
}
.hero h1 {margin: 0; font-size: 2.4rem; font-weight: 800; letter-spacing: 0.5px; color: #fff;}
.hero p {margin: 0.4rem 0 0 0; opacity: 0.92; font-size: 1.02rem;}

div[data-testid="stTextArea"] textarea {
    border-radius: 14px;
    font-size: 0.98rem;
}
div.stButton > button {
    width: 100%;
    border: none;
    border-radius: 14px;
    padding: 0.7rem 1rem;
    font-weight: 700;
    font-size: 1.05rem;
    color: #fff;
    background: linear-gradient(90deg, #7F00FF, #E100FF);
    transition: transform .15s ease, box-shadow .15s ease;
}
div.stButton > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 20px rgba(225, 0, 255, 0.35);
    color: #fff;
}

.card {
    border-radius: 22px;
    padding: 1.8rem;
    margin-top: 1.5rem;
    background: rgba(127, 127, 127, 0.08);
    border: 1px solid rgba(127, 127, 127, 0.22);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.12);
}
.card-top {display: flex; justify-content: space-between; align-items: center; gap: 1rem;}
.title {font-size: 2rem; font-weight: 800; line-height: 1.15; margin: 0;}
.year {
    display: inline-block; margin-top: .5rem; padding: .2rem .8rem;
    border-radius: 999px; font-size: .85rem; font-weight: 600;
    background: rgba(127, 0, 255, 0.15); color: #B266FF;
}
.rating {
    flex-shrink: 0; width: 84px; height: 84px; border-radius: 50%;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
    background: linear-gradient(135deg, #FFB800, #FF512F);
    color: #fff; font-weight: 800; font-size: 1.5rem;
    box-shadow: 0 6px 16px rgba(255, 140, 0, 0.4);
}
.rating small {font-size: .62rem; font-weight: 600; opacity: .9; letter-spacing: 1px;}

.label {
    margin: 1.4rem 0 .5rem 0; font-size: .75rem; font-weight: 700;
    letter-spacing: 1.5px; text-transform: uppercase; opacity: .6;
}
.chip {
    display: inline-block; margin: 0 .4rem .4rem 0; padding: .3rem .9rem;
    border-radius: 999px; font-size: .88rem; font-weight: 600;
}
.chip.genre {background: rgba(255, 81, 47, 0.15); color: #FF7A5C;}
.chip.cast  {background: rgba(0, 180, 216, 0.15); color: #2FC4E0;}
.person {font-size: 1.1rem; font-weight: 600;}
.muted {opacity: .5; font-style: italic;}
.summary {
    margin-top: .2rem; padding: 1rem 1.2rem; border-radius: 14px;
    border-left: 5px solid #E100FF; background: rgba(225, 0, 255, 0.07);
    line-height: 1.6; font-size: 1rem;
}
</style>
""", unsafe_allow_html=True)


# ------------------------------------------------------------------ helpers
def esc(x) -> str:
    return html.escape(str(x))


def chips(items, kind):
    if not items:
        return '<span class="muted">Not mentioned</span>'
    return "".join(f'<span class="chip {kind}">{esc(i)}</span>' for i in items)


def movie_card(m: Movie) -> str:
    year = f'<span class="year">📅 {esc(m.release_year)}</span>' if m.release_year else ""
    rating = (
        f'<div class="rating">{esc(m.rating)}<small>RATING</small></div>'
        if m.rating is not None else ""
    )
    director = (
        f'<span class="person">🎬 {esc(m.director)}</span>'
        if m.director else '<span class="muted">Not mentioned</span>'
    )
    return (
        '<div class="card">'
        '<div class="card-top">'
        f'<div><p class="title">{esc(m.title)}</p>{year}</div>'
        f'{rating}'
        '</div>'
        f'<div class="label">Genre</div>{chips(m.genre, "genre")}'
        f'<div class="label">Director</div>{director}'
        f'<div class="label">Cast</div>{chips(m.cast, "cast")}'
        f'<div class="label">Summary</div><div class="summary">{esc(m.summary)}</div>'
        '</div>'
    )


# ------------------------------------------------------------------ sidebar
with st.sidebar:
    st.header("🎬 CineScan")
    st.write("Paste a paragraph about any movie and get its details as a clean card.")
    st.caption("Extracts: title, year, genre, director, cast, rating & summary.")

# --------------------------------------------------------------------- main
st.markdown(
    '<div class="hero"><h1>🎬 CineScan</h1>'
    '<p>Turn any movie paragraph into structured information</p></div>',
    unsafe_allow_html=True,
)

para = st.text_area(
    "Give Your Paragraph",
    height=200,
    placeholder="Paste your movie paragraph here...",
)

if st.button("✨ Extract Movie Info"):
    if not para.strip():
        st.warning("Please paste a paragraph first.")
    else:
        with st.spinner("Reading the paragraph..."):
            final_prompt = prompt.invoke({
                "paragraph": para,
                "format_instructions": parser.get_format_instructions(),
            })
            response = model.invoke(final_prompt)
            output = response.text

        # Show the same output as the console version, in a nice card
        try:
            movie = parser.parse(output)
            st.markdown(movie_card(movie), unsafe_allow_html=True)
        except Exception:
            st.error("Couldn't format the result, showing the raw output instead.")
            st.code(output)

        with st.expander("Raw model output"):
            st.code(output, language="json")