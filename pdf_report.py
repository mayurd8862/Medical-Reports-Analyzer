
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
import os
import json
from PyPDF2 import PdfReader
import getpass

# Set up Google API Key
GOOGLE_API_KEY = st.secrets.GOOGLE_API_KEY
llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key=GOOGLE_API_KEY)

# llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key="Your API key")

# Streamlit UI for uploading resume
st.title("📋 Medical Reports analyzer")
st.subheader("",divider = 'rainbow')
uploaded_file = st.file_uploader("Upload your resume", type=["pdf"])

if uploaded_file is not None:
    # Read the file content using PyPDF2
    pdf_reader = PdfReader(uploaded_file)
    report_content = ""
    for page in pdf_reader.pages:
        report_content += page.extract_text()
    
    
    prompt = f"""
    You are an AI model that analyzes medical reports. Analyze the following report to extract relevant information in a structured way, ensuring no personally identifiable information is included.

    Here is the medical report content:
    {report_content}

    Provide the output in a clear, structured format with fields deemed relevant and appropriate to the use case. Ensure the extracted data is accurate and appropriate for validation by health professionals.

    """
    
    # Invoke the language model
    result = llm.invoke(prompt)
    
    st.write(result.content)