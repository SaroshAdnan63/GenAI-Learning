from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model
model = init_chat_model("google_genai:gemini-3.5-flash",temperature=1)
response=model.invoke("Daayra Movie review")
print(response.content[0]["text"])
