import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)

from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

st.title("Chatbot")

# Model is created once and reused across reruns
@st.cache_resource
def get_model():
    return init_chat_model("google_genai:gemini-3.6-flash")

model = get_model()

# Mood options (same prompts as the console version)
MOODS = {
    "Sad": "You are a sad AI agent",
    "Funny": "You are a funny AI agent",
    "Angry": "You are an angry AI agent",
    "Helpful": "You are a helpful AI agent",
}

# Mood selector
mood = st.sidebar.selectbox("Choose agent mood", list(MOODS.keys()), index=0)

# Start (or restart) the chat whenever the mood changes
if "messages" not in st.session_state or st.session_state.get("mood") != mood:
    st.session_state.mood = mood
    st.session_state.messages = [SystemMessage(content=MOODS[mood])]

# Show previous messages (skip the system message)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Input box
prompt = st.chat_input("You :")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.text))
    with st.chat_message("assistant"):
        st.markdown(response.text)