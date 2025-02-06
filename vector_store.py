import os
from langchain_community.vectorstores import FAISS  #Updated Import
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.docstore.document import Document
from langchain_huggingface import HuggingFaceEmbeddings  #Correct Import

# Load extracted text
with open("extracted_data.txt", "r", encoding="utf-8") as f:
    text_data = f.read()

# Split text for better embeddings
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
documents = text_splitter.split_text(text_data)
docs = [Document(page_content=chunk) for chunk in documents]

#Use Hugging Face embeddings (free, no API key required)
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Store embeddings in FAISS
vector_store = FAISS.from_documents(docs, embeddings)

# Save FAISS index
vector_store.save_local("faiss_index")

print("Embeddings created and saved successfully!")

