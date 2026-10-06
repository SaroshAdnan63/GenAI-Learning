# GEN-AI Learning

This repository contains my daily learning and practice in Generative AI.

I am learning concepts step by step and implementing them using Python, LangChain, and different LLM providers.

---

##  Day 1 — Getting Started with GenAI

### What I Learned

* Set up Python environment using **uv**
* Created a virtual environment
* Installed **LangChain**
* Connected LangChain with **Google Gemini**
* Learned the basics of **LLMs**
* Learned what **LangChain** is
* Learned how to invoke an LLM

---

## Day 2 — Embeddings, Chatbot & LangChain Messages

### What I Learned

* Learned the basics of **Embedding Models**
* Learned how text can be converted into numerical representations called **embeddings**
* Created my first simple **AI chatbot**
* Learned how conversation history works
* Learned about LangChain Core message types:

  * `HumanMessage`
  * `AIMessage`
  * `SystemMessage`

### LangChain Message Flow


SystemMessage
      ↓
HumanMessage
      ↓
AIMessage
      ↓
HumanMessage
      ↓
AIMessage

### What I Practiced

* Working with embedding models
* Creating a basic chatbot
* Passing conversation history to an LLM
* Using `HumanMessage`
* Using `AIMessage`
* Using `SystemMessage`

---

## Tech Stack

* Python
* LangChain
* Google Gemini
* OpenAI
* Groq
* Mistral
* uv

---

##  Project Structure

```text
Generative AI/
│
├── chatmodels/
|   |_chat.py
│   └── chatbot.py
|   |_huggingface.py
|   |_UIchatbot.py
│
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock


📅 Day 3 — Streamlit & Mood-Based Chatbot UI
What I Learned

Today I learned the basics of Streamlit and how it can be used to create a simple web-based user interface using Python.
I also created a Mood-Based Chatbot where the user can choose the mood/personality of the AI agent before starting the conversation.

Mood Options
The user can choose between:
 Sad Mood
 Funny Mood
Angry Mood

Based on the selected mood, a different SystemMessage is passed to the LLM to control how the chatbot responds.


📅 Day 4 — Structured Prompts & Movie Information Extractor
What I Learned

Today I learned about Structured Prompts and how prompts can be designed with clear instructions and input variables.

I also started working on a Movie Information Extractor using LangChain.

Structured Prompts

I learned how to create prompts with separate sections for:

System instructions
Human input
Dynamic variables

Instead of writing one large hard-coded prompt, structured prompts allow me to organize instructions and user input more clearly.

For example:

System
  ↓
Instructions for the AI
  ↓
Human
  ↓
Movie information provided by the user
  ↓
LLM
  ↓
Structured movie information

Movie Information Extractor 
I started building a simple application that takes information about a movie and asks the LLM to extract the useful information from it.
The goal is to convert unstructured movie-related text into useful structured information.

What I Practiced
Creating structured prompts with LangChain
Using ChatPromptTemplate
Creating system and human prompt messages


##  Goal

To build a strong understanding of Generative AI concepts and gradually create real-world applications using LLMs, LangChain, embeddings, RAG, agents, and other GenAI technologies.
