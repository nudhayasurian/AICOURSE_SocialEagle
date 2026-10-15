from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

#load API key from .env file to kernel
load_dotenv(dotenv_path="AI/.env")
#fetch the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize LangChain model
model = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
    temperature=0
)

#response = model.invoke("Explain LangSmith in simple terms.")

#print("AI Response:", response.content)
prompts = ["give me 5 healthy breakfast ideas"
           ] 

for p in prompts:
    response = model.invoke(p)
    print("AI Response:", response.content)
    