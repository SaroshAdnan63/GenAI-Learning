from langchain_huggingface import  HuggingFaceEmbeddings
from dotenv import load_dotenv
load_dotenv

embedding=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

texts=[
    "Hello i am Sarosh",
    "what are you learning today",
    "What's going on ?"
]

vector=embedding.embeded_documents(texts)