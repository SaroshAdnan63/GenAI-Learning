from dotenv import load_dotenv
load_dotenv()
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
llm=HuggingFaceEndpoint(
    repo_id="deepseek-ai/DeepSeek-R1"
)
model = ChatHuggingFace(llm=llm)
response=model.invoke("Best Malayam thriller movies to watch")
print(response.content)