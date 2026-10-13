from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

#load API key from .env file to kernel
load_dotenv(dotenv_path="AI/.env")

#fetch the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

#1. prompt template with a blank {topic} to be filled in with the retrieved documents
prompt_template = ChatPromptTemplate.from_template("Explain {topic} in one simple sentence")

#2. model initialization with the OpenAI API key
model = ChatOpenAI(model="gpt-3.5-turbo", api_key=api_key, temperature=0.7, max_tokens=100)

#3. output parser initialization to parse the model's output into a string
output_parser = StrOutputParser()

print("Prompt template, model, and output parser initialized successfully") 

chain = prompt_template | model | output_parser
print("Chain created successfully")

answer = chain.invoke({"topic": "Python programming language"})
print("Answer from the chain:", answer)







