import validators
import streamlit as st
from langchain.chains.summarize import load_summarize_chain


import os
from dotenv import load_dotenv
load_dotenv()


from loader import data_loader
from config import llm_model, stuff_prompt, map_prompt, combine_prompt



st.set_page_config(page_title="Website Text Summarizer")
st.title("LangChain-Powered Web Summarizer")
st.subheader("Provide a URL to summarize the content within seconds !")




api_key = os.getenv("GROQ_API_KEY")



url = st.text_input("URL", label_visibility="collapsed")

summarization_method = st.selectbox(
    "Choose summarization method for long content:",
    ["Map-Reduce", "Stuff"]
)




if st.button("Summarize the content"):
    if not url.strip():
        st.error("Please enter a URL to get started")
    elif not validators.url(url):
        st.error("Please enter a valid URL")

    else:
        try:
            with st.spinner("Waiting..."):
                ##loading the data
                docs = data_loader(url)
                #chain
                if summarization_method == "Stuff":
                    chain_type = "stuff"

                elif summarization_method == "Map-Reduce":
                    chain_type = "map_reduce"

                #summary chain declaration
                with st.spinner("Just a moment..."):

                    with st.spinner("Calibrating the chain type..."):

                        if chain_type=="stuff":
                            chain = load_summarize_chain(llm= llm_model,
                                                        chain_type="stuff",
                                                        prompt=stuff_prompt)
                        else:
                            chain = load_summarize_chain(llm= llm_model,
                                                        chain_type="map_reduce",
                                                        map_prompt=map_prompt,
                                                        combine_prompt= combine_prompt,
                                                        verbose = True)
                     
                    output_summary = chain.run(docs)
                    
                    st.success("Your summary is successfully generated ! Take a look...")
                    st.write(output_summary)

        except Exception as e:
            st.exception(f"Exception: {e}")


        