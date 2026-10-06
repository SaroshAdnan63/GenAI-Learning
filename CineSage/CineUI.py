import re
import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)

import streamlit as st
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
from langchain.chat_models import init_chat_model

# ---------------------------------------------------------------- page setup
st.set_page_config(page_title="Movie Info Extractor", page_icon="🎬", layout="wide")


@st.cache_resource
def get_model():
    return init_chat_model("google_genai:gemini-3.6-flash")


model = get_model()

# ------------------------------------------------------------------- prompt
prompt = ChatPromptTemplate.from_messages([

    # System Message
    (
    "system",
"""
You are an intelligent information extraction and summarization assistant.
Your task is to analyze the paragraph provided by the user and extract the most useful and relevant information from it.
You specialize in extracting structured information from movie-related content and generating concise summaries.

Return the information in the following format:
Movie Name: [Movie name if mentioned, otherwise "Not mentioned"]

Genre: [Genre or genres]

Release Date: [Release date]

Director: [Director name]

Producer / Production House: [Producer or production company if mentioned]

Lead Actors: [Main male actors]

Lead Actresses: [Main female actors/actresses]

Cast: [Other important cast members]

Budget: [Movie budget]

Box Office Collection: [Box office collection and time period if mentioned]

IMDb Rating: [IMDb rating if mentioned]

Plot: [2-3 sentence description of the story]

Commercial/Critical Reception: [Brief information about the movie's success, reviews, or reception]

Quick Summary: [Give a concise 2-3 sentence summary of the entire paragraph]

Important Information: [Mention any other useful information that does not fit into the above fields]

Rules:

1. Extract only information that is explicitly present in the paragraph.
2. Do not invent or assume missing information.
3. If a field is not available, write "Not mentioned".
4. Keep the extracted information concise and easy to understand.
5. For the Quick Summary, combine the most important points into a short, readable summary.
6. Preserve numbers, dates, ratings, and monetary values accurately.
7. Do not provide unnecessary explanations.
8. Distinguish between actors/actresses and general cast when possible.
9. If multiple directors, producers, or production houses are mentioned, include all relevant names.
10. For Box Office Collection, include the amount and specify whether it is worldwide, domestic, opening day, first week, etc., if mentioned.
11. Do not use outside knowledge to fill missing information.
12. Maintain the same meaning as the original paragraph while making the extracted information concise.
"""
),
    # Human Message
    (
        "human",
        """
Analyze the following paragraph and extract the useful information according to the instructions.
Paragraph:{paragraph}
"""
)
])

# ------------------------------------------------------------------ helpers
FIELDS = [
    "Movie Name", "Genre", "Release Date", "Director",
    "Producer / Production House", "Lead Actors", "Lead Actresses", "Cast",
    "Budget", "Box Office Collection", "IMDb Rating", "Plot",
    "Commercial/Critical Reception", "Quick Summary", "Important Information",
]


def parse_output(text: str) -> dict:
    """Turn the model's 'Field: value' output into a dict."""
    pattern = re.compile(
        r"^\W*(" + "|".join(re.escape(f) for f in FIELDS) + r")\W*:\s*(.*)$",
        re.IGNORECASE,
    )
    data, current = {}, None
    for line in text.splitlines():
        m = pattern.match(line.strip())
        if m:
            current = next(f for f in FIELDS if f.lower() == m.group(1).lower())
            data[current] = m.group(2).strip().strip("*").strip()
        elif current and line.strip():
            data[current] += " " + line.strip()
    return data


def show(data: dict, key: str, container=None):
    """Show a labelled field."""
    c = container or st
    c.markdown(f"**{key}**")
    c.write(data.get(key, "Not mentioned") or "Not mentioned")


# ------------------------------------------------------------------ sidebar
with st.sidebar:
    st.header("About")
    st.write(
        "Paste any movie-related paragraph and get the key details "
        "(cast, budget, box office, plot, etc.) in a clean format."
    )
    st.caption("Only information present in the paragraph is extracted.")

# --------------------------------------------------------------------- main
st.title("🎬 Movie Info Extractor")
st.write("Paste a paragraph about a movie and extract structured information from it.")

para = st.text_area(
    "Give Your Paragraph",
    height=220,
    placeholder="Paste your movie paragraph here...",
)

extract = st.button("Extract Information", type="primary")

if extract:
    if not para.strip():
        st.warning("Please paste a paragraph first.")
    else:
        with st.spinner("Extracting information..."):
            final_prompt = prompt.invoke({"paragraph": para})
            response = model.invoke(final_prompt)
            output = response.text

        data = parse_output(output)

        st.divider()

        if len(data) < 5:
            # Fallback if the output isn't in the expected format
            st.subheader("Result")
            st.markdown(output)
        else:
            # Title row
            st.header(data.get("Movie Name", "Not mentioned"))

            c1, c2, c3 = st.columns(3)
            show(data, "Genre", c1)
            show(data, "Release Date", c2)
            show(data, "IMDb Rating", c3)

            st.subheader("Crew")
            c1, c2 = st.columns(2)
            show(data, "Director", c1)
            show(data, "Producer / Production House", c2)

            st.subheader("Cast")
            c1, c2, c3 = st.columns(3)
            show(data, "Lead Actors", c1)
            show(data, "Lead Actresses", c2)
            show(data, "Cast", c3)

            st.subheader("Money")
            c1, c2 = st.columns(2)
            show(data, "Budget", c1)
            show(data, "Box Office Collection", c2)

            st.subheader("Story & Reception")
            show(data, "Plot")
            st.write("")
            show(data, "Commercial/Critical Reception")

            st.subheader("Summary")
            st.info(data.get("Quick Summary", "Not mentioned"))

            st.subheader("Other Details")
            st.write(data.get("Important Information", "Not mentioned"))

        with st.expander("Raw model output"):
            st.text(output)