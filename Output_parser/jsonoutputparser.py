from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser



load_dotenv()


model = ChatGroq(model = 'meta-llama/llama-4-scout-17b-16e-instruct')

parser = JsonOutputParser()

template = PromptTemplate(
    template = 'Give me the name, age and city of the fictional person \n {format_instructions}',
    input_variables=[],
    partial_variables = {'format_instructions': parser.get_format_instructions() }
)

chain = template | model | parser

result = chain.invoke({})

print(result)