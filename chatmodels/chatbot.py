import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = init_chat_model("google_genai:gemini-3.6-flash")

print("Choose agent Mood")

print("Choose 1 for sad Mood")
print("Choose 2 for funny Mood")
print("Choose 3 for angry  Mood")

choice = input("Choose your agent mood: ")

if choice == "1":
    mode = SystemMessage(content="You are a sad AI agent")

elif choice == "2":
    mode = SystemMessage(content="You are a funny AI agent")

elif choice == "3":
    mode = SystemMessage(content="You are an angry AI agent")

else:
    mode = SystemMessage(content="You are a helpful AI agent")
    
messages=[mode]
while True:
    prompt=input("You :")
    if prompt=="0":
        break
    messages.append(HumanMessage(content=prompt))
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.text))
    print("Bot :",response.text)

