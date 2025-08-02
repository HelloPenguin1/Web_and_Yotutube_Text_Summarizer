import validators
import streamlit as st



import os
from dotenv import load_dotenv
load_dotenv()


from loader import data_loader
from config import calibrate_chain_type



st.set_page_config(page_title="Website Text Summarizer")
st.title("LangChain-Powered Web Summarizer")
st.subheader("Provide a URL to summarize the content within seconds !")




api_key = os.getenv("GROQ_API_KEY")



url = st.text_input("URL", label_visibility="collapsed")

summarization_method = st.selectbox(
    "Select Summarization Strategy:",
    ["Stuff", "Map-Reduce"],
    help=(
        "🧾 **Stuff**: Loads all content at once. Best for short or simple texts "
        "(e.g., single blog posts, brief articles).\n\n"
        "🧠 **Map-Reduce**: Splits content into chunks, summarizes each one individually "
        "(Map), then combines those summaries into a final summary (Reduce). Ideal for "
        "large documents, multiple articles, or when token limits are a concern."
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

                if summarization_method == "Stuff":
                    chain_type = "stuff"

                elif summarization_method == "Map-Reduce":
                    chain_type = "map_reduce"


                #summary chain declaration   
                chain = calibrate_chain_type(chain_type)

                output_summary = chain.run(docs)
                    
                st.success("Your summary is successfully generated! Take a look...")
                st.write(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")


        