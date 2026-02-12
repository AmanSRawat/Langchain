from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
      template = "Generate 5 interesting facts about {topic}.",
      input_variables= ['topic']
)

model = ChatGroq(model = 'meta-llama/llama-4-scout-17b-16e-instruct')

parser = StrOutputParser()

chain = prompt | model | parser

result = chain.invoke({'topic': 'black hole'})

print(result)
chain.get_graph().print_ascii()