from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template= 'Generate the detaield report on the {topic}.',
    input_variables= ['topic']
)

prompt2 = PromptTemplate(
    template = 'Generate the 5 point summary of the following text \n {text}',
    input_variables= [ 'text']
)

parser = StrOutputParser()

model = ChatGroq(model = 'meta-llama/llama-4-scout-17b-16e-instruct')

chain = prompt1 | model | parser | prompt2 | model | parser

result = chain.invoke({'topic': 'unemployment in India'})

print(result)

chain.get_graph().print_ascii()