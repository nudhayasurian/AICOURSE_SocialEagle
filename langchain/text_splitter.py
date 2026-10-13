from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
import os

#load API key from .env file to kernel
load_dotenv(dotenv_path="AI/.env")

#fetch the API key from environment variable
api_key = os.getenv("OPENAI_API_KEY")

#initialize the OpenAIEmbeddings model with the API key
embeddings = OpenAIEmbeddings(model="text-embedding-3-small", api_key=api_key)
print("OPENAI EMBEDDINGS model is ready")

#initialize the RecursiveCharacterTextSplitter with chunk size and overlap
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=2
)

#load the text data from the file and split it into chunks
document = TextLoader("langchain/data.txt").load()
chunks = text_splitter.split_documents(document)
print("Text chunks:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}") 

#generate embeddings for each chunk and print the vector and its length
vector = embeddings.embed_query(chunk.page_content)

#for i, vector in enumerate(vectors):
print(f"Vector for chunk {i}: {vector}")
print(f"Vector length for chunk {i}: {len(vector)}")

vectorstore = FAISS.from_documents(chunks, embeddings)  
print("FAISS vectorstore created successfully")

#test vextorstore by performing a similarity search with a query
query = "Describe the cultural significance of Pongal celebration in Tamil Nadu."
results = vectorstore.similarity_search(query, k=3)

print("Similarity search results:")
for i, result in enumerate(results):
    print(f"Result {i}: {result.page_content}") 

#store it locally for future use
vectorstore.save_local("langchain/vectorstore")

#load the vectorstore from local storage and perform a similarity search with a query
loaded_vectorstore = FAISS.load_local("langchain/vectorstore", embeddings, allow_dangerous_deserialization=True)

#retrieve the top 3 most similar documents to the query using the loaded vectorstore
retriever = loaded_vectorstore.as_retriever(search_kwargs={"k": 3})
print("Retriever created successfully")

#query the retriever with a question and print the retrieved documents
question = "tell me about tamil nadu?"
retrieved_docs = retriever.invoke(question) 

print("question:", question)
for i, doc in enumerate(retrieved_docs):
    print(f"Document {i}: {doc.page_content}")

#chaining















