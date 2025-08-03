import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from prompts import stuff_prompt, map_prompt, combine_prompt, question_prompt, refine_prompt

import streamlit as st

def get_groq_api_key():
    try:
        return st.secrets["GROQ_API_KEY"]
    except:
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            st.error("GROQ_API_KEY not found")
            st.stop()
        return api_key
    

# LLM Model
llm_model = ChatGroq(
    api_key=get_groq_api_key(),
    model_name='Gemma2-9b-It',
    streaming=True
)

# Chain Type 
def calibrate_chain_type(chain_type):
    if chain_type=="stuff":
        chain = load_summarize_chain(llm= llm_model, 
                                     chain_type="stuff",
                                     prompt=stuff_prompt,
                                     verbose = True)
    elif chain_type=="map_reduce":
        chain = load_summarize_chain(llm= llm_model, chain_type="map_reduce",
                                                 map_prompt=map_prompt,
                                                 combine_prompt= combine_prompt,
                                                 verbose = True)
    else:
        chain = load_summarize_chain(llm= llm_model, 
                                     chain_type="refine",
                                     question_prompt = question_prompt,
                                     refine_prompt = refine_prompt,
                                     verbose = True)
    
    return chain

