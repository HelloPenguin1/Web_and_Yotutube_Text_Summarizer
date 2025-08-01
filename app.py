import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader, UnstructuredURLoader
import os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="Youtube and Website Text Summarizer")
st.title("LangChain-Powered Web and Youtube Summarizer")
st.subheader("Provide a URL to summarize the content within seconds !")

api_key = os.getenv("GROQ_API_KEY")