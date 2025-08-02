import validators
import streamlit as st



import os
from dotenv import load_dotenv
load_dotenv()


from loader import data_loader
from config import calibrate_chain_type



st.set_page_config(page_title="Website Text Summarizer")
st.title("LangChain-Powered Web Summarizer")
st.write("Provide a URL to summarize the content within seconds !")




api_key = os.getenv("GROQ_API_KEY")



url = st.text_input("URL", label_visibility="collapsed")

summarization_method = st.selectbox(
    "Select Summarization Strategy:",
    ["Stuff Technique", "Map-Reduce Technique"],
    help=(
        "**Stuff**: Loads all content at once. Best for short or simple texts "
        "(e.g., single blog posts, brief articles).\n\n"
        "**Map-Reduce**: Splits content into chunks, summarizes each one individually, "
        "then combines those summaries into a final summary. Ideal for large documents"
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


                #summary chain declaration   
                chain = calibrate_chain_type(chain_type)

                output_summary = chain.run(docs)
                    
                st.success("Your summary is successfully generated! Take a look...")
                st.write(output_summary)

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
    


        