# PDF Retrieval Text Augmented Generation
This document describes a Streamlit application that allows users to search for information within a PDF document.

## Description
The application leverages OpenAI's large text embedding model to process the text content of the uploaded PDF. It then utilizes a retrieval chain to search for relevant passages based on the user's query.

## Code Breakdown
### Imports
- streamlit as st: Streamlit for creating the web application.
- os: Python library for interacting with the operating system.
- tempfile: Provides temporary files and directories.
- chromadb: Library for managing vector databases.
- langchain_community.vectorstores: Provides vector store implementations.
- langchain_community.document_loaders: Provides document loaders for different file formats.
- langchain_openai: Enables access to OpenAI's API.
- langchain.chains.conversational_retrieval.base: Provides base class for conversational retrieval chains.

### Enviornment variables
The OpenAI API key needs to be set as an environment variable:
~~~python
os.environ["OPENAI_API_KEY"] = ""
~~~
Replace the empty string with your actual OpenAI API key.

### Embeddings
The code initializes the OpenAI embedding model for text:
~~~python
 embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
~~~
This model will be used to generate embeddings for the extracted PDF text.

### functions
#### get_docs(file):
- Takes a PDF file and returns a list of extracted pages.
- Creates a temporary file to store the uploaded PDF content.
- Uses PyPDFLoader to load and split the PDF document into separate pages.
- 
#### embed(documents):
- Takes a list of documents (pages) and returns a Chroma vector database.
- Creates a Chroma vector database using the provided documents and embeddings.
- The persist_directory argument specifies the directory where the database will be persisted.
#### search(query, db):
- Takes a query string and a Chroma vector database as input and returns the answer to the query.
- Creates an OpenAI instance with a temperature of 0.8.
- Creates a ChatVectorDBChain instance using the OpenAI model and the Chroma database for retrieval in a conversational setting.
- Constructs a query object with the user's query and an empty chat history.
- Uses the pdf_qa object to perform the search and retrieves the answer.

### Streamlit App
The app title is set to "PDF Text Retrieval Augmented Generation".
- A file uploader allows users to upload a PDF document.
- A text input field allows users to enter their query.
- The app checks for user actions:
  1. File Upload:
  2. If a file is uploaded, the get_docs function extracts the text.
  3. If text extraction is successful, the embed function creates the vector database.
  4. Success/Error messages are displayed based on the upload status.

#### Query Input:
- If a query is entered, a spinner indicates search progress.
- The search function retrieves the answer based on the query and the database.
- The retrieved answer is displayed on the Streamlit app.

## Requirements
Python
Streamlit library
OpenAI API key
langchain libraries

## How to Use
Install Python and required libraries.
Set your OpenAI API key.
Run the script.
Upload a PDF document and enter your query in the Streamlit app.
Click the search button to see the retrieved answer.


