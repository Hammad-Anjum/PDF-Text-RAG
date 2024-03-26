import streamlit as st
import os 
import tempfile
import chromadb
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import OpenAIEmbeddings
from langchain.chains.conversational_retrieval.base import ChatVectorDBChain
from langchain_openai import OpenAI

persist_directory = "chroma_db" 

os.environ["OPENAI_API_KEY"] = ""
embeddings = OpenAIEmbeddings(model="text-embedding-3-large") #embedding model


def get_docs(file):

    with tempfile.NamedTemporaryFile(delete=False) as tmp_file: #create temp file to access original file
            tmp_file.write(file.read())
            tmp_file_path = tmp_file.name #save the name as the path

    loader = PyPDFLoader(tmp_file_path)
    pages = loader.load_and_split() #pyPDFLoader to load and split the data

    return pages

def embed(docs):

    db = Chroma.from_documents(docs , embeddings , persist_directory = persist_directory) #store in directory using the extracted docs and embeddings
    return db


def search(query , db):
    model = OpenAI(temperature=0.8)  # Create OpenAI instance

    pdf_qa = ChatVectorDBChain.from_llm(model, db, return_source_documents=True) #using DBchain to query

    result = pdf_qa({"question": query, "chat_history": ""})

    return result["answer"]

    

st.title("PDF Text Retrieval Augmented Generation")

file = st.file_uploader("Upload the PDF" , type= 'pdf')
query = st.text_input("Enter query :" , max_chars= 256)

if file:
    print("yes")
    text = get_docs(file)
    if text:
        db = embed(text)
        st.success('File uploaded and embedded!')
    else:
        st.error("Please upload a PDF file.")
    
if query:
    with st.spinner("Searching..."):  
        text = search(query, db) 
    st.text(text)





