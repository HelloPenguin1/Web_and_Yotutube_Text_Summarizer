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

# Stuff Prompt Template
stuff_prompt_template = """
You are an expert text summarizer. 
Provide a summary of the following content in 300 words based on the given directions.
Directions: 
1) Be as accurate as possible while referencing the source content. 
2) Openly use bullet points when necessary to separate complicated details into manageable chunks.
3) Clarify a complicated concept in simpler words.

Content:{text}
"""

stuff_prompt = PromptTemplate(template=stuff_prompt_template,
                        input_variables=['text'])


#Map-Reduce prompts


# Map prompt template (for individual chunk processing in map-reduce)
map_prompt_template = """
You are an expert text summarizer. 
Create a concise summary of the following text chunk. Focus on the main points and key information.

Text chunk:
{text}

Summary:
"""

map_prompt = PromptTemplate(template=map_prompt_template, input_variables=['text'])

# Combine prompt template (for final summarization in map-reduce)
combine_prompt_template = """
You are an expert text summarizer. 
The following are summaries of different sections of a larger document.
Combine these summaries into a comprehensive final summary of 300 words.

Directions: 
1) Be as accurate as possible while referencing the source content. 
2) Openly use bullet points when necessary to separate complicated details into manageable chunks.
3) Clarify a complicated concept in simpler words.
4) Ensure the final summary flows well and covers all major points from the individual summaries.

Summaries to combine:
{text}

Final comprehensive summary:
"""

combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=['text'])