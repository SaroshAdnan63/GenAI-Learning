# GEN-AI Learning

This repository contains my daily learning and practice in Generative AI.

I am learning concepts step by step and implementing them using Python, LangChain, and different LLM providers.

---

##  Day 1 — Getting Started with GenAI


* Set up Python environment using **uv**
* Created a virtual environment
* Installed **LangChain**
* Connected LangChain with **Google Gemini**
* Learned the basics of **LLMs**
* Learned what **LangChain** is
* Learned how to invoke an LLM

---

## Day 2 — Embeddings, Chatbot & LangChain Messages



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


Today I learned the basics of Streamlit and how it can be used to create a simple web-based user interface using Python.
I also created a Mood-Based Chatbot where the user can choose the mood/personality of the AI agent before starting the conversation.

Mood Options
The user can choose between:
 Sad Mood
 Funny Mood
Angry Mood

Based on the selected mood, a different SystemMessage is passed to the LLM to control how the chatbot responds.


📅 Day 4 — Structured Prompts & Movie Information Extractor


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

Practiced:
Creating structured prompts with LangChain
Using ChatPromptTemplate
Creating system and human prompt messages


📅 Day 5 — Structured Output & JSON Schema


Today I learned about Structured Output and how to get an LLM to return information in a predefined format instead of plain text.

I learned how to use Pydantic with LangChain to define the structure of the expected output.

PydanticOutputParser

I learned how to use PydanticOutputParser to:

Define the expected output structure using a Pydantic model
Generate formatting instructions for the LLM
Parse the LLM's response into a structured Python object
Work with different data types such as str, int, float, and List


📅 Day 6 — Understanding RAG (Retrieval-Augmented Generation)


Today I learned about RAG (Retrieval-Augmented Generation), an important concept in Generative AI that helps LLMs generate responses using relevant information retrieved from external documents or knowledge sources.

What Is RAG?
RAG combines two main processes:

Retrieval: Finds relevant information from a knowledge source based on the user's query.
Generation: Uses the retrieved information as context to generate an answer with an LLM.
How RAG Works
User Question
      ↓
Retrieve Relevant Information
      ↓
Pass Information as Context
      ↓
LLM Generates an Answer
      ↓
Final Response
Key Concepts I Learned
The basics of Retrieval-Augmented Generation
Why RAG is useful in LLM applications
How external knowledge can provide context to an LLM
How retrieval and generation work together
How RAG can help answer questions using custom documents

##  Goal

To build a strong understanding of Generative AI concepts and gradually create real-world applications using LLMs, LangChain, embeddings, RAG, agents, and other GenAI technologies.
