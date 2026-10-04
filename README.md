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
│   └── chat.py
│
├── .gitignore
├── README.md
├── pyproject.toml
└── uv.lock




##  Goal

To build a strong understanding of Generative AI concepts and gradually create real-world applications using LLMs, LangChain, embeddings, RAG, agents, and other GenAI technologies.
