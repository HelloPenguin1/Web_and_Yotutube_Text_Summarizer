from langchain.prompts import PromptTemplate

# Stuff Prompt Template
stuff_prompt_template = """
You are an expert text summarizer. 
Provide a summary of the following content in 300 words based on the given directions.
Directions: 
1) Be as accurate as possible while referencing the source content. 
2) Openly use bullet points when necessary to separate complicated details into manageable chunks.
3) Clarify a complicated concept in simpler words.
5) Add a bolded title on top of the summary
6) Below the title, mention the name of the website and the author (if any) and the date it was published.

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
5) Add a bolded title on top of the summary
6) Below the title, mention the name of the website and the author (if any) and the date it was published.

Summaries to combine:
{text}

Final comprehensive summary:
"""

combine_prompt = PromptTemplate(template=combine_prompt_template, input_variables=['text'])



# Refine summarization prompt
question_prompt_temp = """
You are an expert text summarizer. 
Create a initial summary of the following content. Focus on the main points and key information.

Text chunk:
{text}

Summary:
"""

question_prompt = PromptTemplate(template=question_prompt_temp, input_variables=['text'])



refine_prompt_template = """
You are an expert text summarizer.
You have been provided with an existing summary up to a certain point: {existing_answer}

Now you have to refine the existing summary with some more context below.

New content:
{text}

Given the new context, refine the original summary to create a comprehensive final summary of 300 - 400 words.
If the new content is not relevant, return the original summary unchanged.

Directions: 
1) Be as accurate as possible while referencing the source content. 
2) Openly use bullet points when necessary to separate complicated details into manageable chunks.
3) Clarify a complicated concept in simpler words.
4) Ensure the final summary flows well and covers all information.
5) Add a bolded title on top of the summary
6) Below the title, mention the name of the website and the author (if any) and the date it was published.

Refined summary:

"""

refine_prompt = PromptTemplate(template = refine_prompt_template, 
                               input_variables=['existing_answer', 'text'])
