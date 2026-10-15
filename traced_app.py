from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

#load API key from .env file to kernel
load_dotenv(dotenv_path="AI/.env")
#fetch the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")
# Verify configuration
print("Tracing enabled:", os.getenv("LANGSMITH_TRACING"))
print("LangSmith project:", os.getenv("LANGSMITH_PROJECT"))
#print("OpenAI key configured:", bool(os.getenv(api_key)))
#print("LangSmith key configured:", bool(os.getenv("LANGSMITH_API_KEY")))

# Initialize LangChain model
model = ChatOpenAI(
    model="gpt-4.1-mini",
    api_key=api_key,
    temperature=0
)

#response = model.invoke("Explain LangSmith in simple terms.")

#print("AI Response:", response.content)
prompts = ["Explain LangSmith in simple terms.", 
           "concept of error rate in langsmith",
           "how langsmith can be used to improve model performance","how langsmith can be used to track model performance over time"
          ]  
for p in prompts:
    response = model.invoke(p)
    print("AI Response:", response.content)
    