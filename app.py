import validators
import streamlit as st

import os
from dotenv import load_dotenv
load_dotenv()

from loader import data_loader
from config import calibrate_chain_type

# Title 
st.set_page_config(page_title="Website Text Summarizer")
st.title("LangChain-Powered Web Summarizer")
st.write("Provide a URL to summarize the content within seconds !")

#api key
api_key = os.getenv("GROQ_API_KEY")


#Initializing session state variables
if "summary_result" not in st.session_state:
    st.session_state.summary_result = None
if "url_input" not in st.session_state:
    st.session_state.url_input = None


# URL
url = st.text_input("URL", label_visibility="collapsed", value=st.session_state.url_input)



summarization_method = st.selectbox(
    "Select Summarization Strategy:",
    ["Stuff Technique", "Map-Reduce Technique", "Refine Technique"],
    help=(
        "**Stuff**: Loads all content at once. Best for short or simple texts "
        "(e.g., single blog posts, brief articles).\n\n"
        "**Map-Reduce**: Splits content into chunks, summarizes each one individually, "
        "then combines those summaries into a final summary. Ideal for large documents.\n\n"
        "**Refine (Advanced)** Starts with a base summary and enhances it progressively"
        " by using each new chunk of content. Useful for detailed, accurate summaries."
    )
)


if st.button("Summarize the content"):
    if not url.strip():
        st.error("Please enter a URL to get started")
    elif not validators.url(url):
        st.error("Please enter a valid URL")

    else:
        try:
            with st.spinner("Just a moment..."):
                ##loading the data
                docs = data_loader(url)

                if summarization_method == "Stuff Technique":
                    chain_type = "stuff"

                elif summarization_method == "Map-Reduce Technique":
                    chain_type = "map_reduce"
                
                else:
                    chain_type = "refine"


                #summary chain declaration   
                chain = calibrate_chain_type(chain_type)

                output_summary = chain.run(docs)
                
                #saving value to session state
                st.session_state.summary_result = output_summary

                

        except Exception as e:
            error_message = str(e).lower()
            
            if any(phrase in error_message for phrase in [
                "context_length_exceeded", 
                "reduce the length", 
                "maximum context length",
                "context window",
                "token limit",
                "too long"
            ]):
                st.error("⚠️ Content Too Long for Stuff Technique!")
                st.warning(
                    "The content is too large to process with the **Stuff Technique**. "
                    "Please switch to **Map-Reduce Technique** and try again."
                )
    
# once summary is generated, add option to clear session variables and summary and start fresh
if st.session_state.summary_result:
    st.success("Your summary is successfully generated! Take a look...")
    st.write(st.session_state.summary_result)
    
   
    if st.button("Clear Output", type="secondary", key="clear_output"):
        st.session_state.summary_result = None
        st.session_state.url_input = ""
        st.rerun()

        