import logging
logging.getLogger("google_genai.models").setLevel(logging.ERROR)
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
load_dotenv()
# from langchain.chat_models import init_chat_model
# model = init_chat_model("google_genai:gemini-3.6-flash")
from langchain_mistralai import ChatMistralAI
model=ChatMistralAI(model='mistral-small-4')

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

para=input("Give Your Paragraph : ")
final_prompt=prompt.invoke(
    {"paragraph":para}
)
response=model.invoke(final_prompt)
print(response.text)