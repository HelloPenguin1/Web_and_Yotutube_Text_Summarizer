import os
from dotenv import load_dotenv
load_dotenv()

from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate



# LLM Model
llm_model = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    model_name='Gemma2-9b-It',
    streaming=True
)


#prompt 
prompt_template = """
You are an expert text summarizer. 
Provide a summary of the following content in 300 words based on the given directions.
Directions: 
1) Be as accurate as possible while referencing the source content. 
2) Openly use bullet points when necessary to separate complicated details into manageable chunks.
3) Clarify a complicated concept in simpler words.

Content:{text}
"""

prompt = PromptTemplate(template=prompt_template,
                        input_variables=['text'])