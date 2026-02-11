from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate


load_dotenv()


model = ChatGroq(model = 'meta-llama/llama-4-scout-17b-16e-instruct')

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a five line summary on the following text. \n {text}',
    input_variables=['text']
)

prompt1 = template1.invoke({'topic': 'Black Hole'})

result = model.invoke(prompt1)

prompt2 = template2.invoke({'text': result.content})

result2 = model.invoke(prompt2)

print(result2.content)