import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.messages import HumanMessage,AIMessage,SystemMessage

model = init_chat_model("google_genai:gemini-3.6-flash")


messages=[
    SystemMessage(content="You are a funny ai agent")
]
while True:
    prompt=input("You :")
    messages.append(HumanMessage(content=prompt))
    if prompt=="0":
        break
    response=model.invoke(messages)
    messages.append(AIMessage(content=response.text))
    print("Bot :",response.text)

