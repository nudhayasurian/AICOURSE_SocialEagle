text = """create a scale prompt to genarate an image to describe tamil nadu culture, 
which include pongal celebration, 
challi kattu, madurai meenachi temple, margali kollam, bharatanatiam"""
with open("langchain/data.txt", "w") as f:
    f.write(text)   
    print("Data written to langchain/data.txt")

from langchain_text_splitters import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=20,
    chunk_overlap=2
)
chunks = text_splitter.split_text(text)
print("Text chunks:")
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {chunk}")    
