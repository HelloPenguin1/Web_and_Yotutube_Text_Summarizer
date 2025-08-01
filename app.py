import validators
import streamlit as st
from langchain.chains.summarize import load_summarize_chain


import os
from dotenv import load_dotenv
load_dotenv()


from loader import data_loader
from config import llm_model, prompt



st.set_page_config(page_title="Youtube and Website Text Summarizer")
st.title("LangChain-Powered Web and Youtube Summarizer")
st.subheader("Provide a URL to summarize the content within seconds !")




api_key = os.getenv("GROQ_API_KEY")



url = st.text_input("URL", label_visibility="collapsed")

if st.button("Summarize the content"):
    if not url.strip():
        st.error("Please enter a URL to get started")
    elif not validators.url(url):
        st.error("Please enter a valid URL")
        st.info("URL may be a YouTube video or a website url")

    else:
        try:
            with st.spinner("Waiting..."):
                ##loading the data
                docs = data_loader(url)

                #chain
                chain = load_summarize_chain(llm= llm_model,
                                             chain_type="stuff",
                                             prompt=prompt)
                output_summary = chain.run(docs)
                
                st.success(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")


        