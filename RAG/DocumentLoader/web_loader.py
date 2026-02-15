from langchain_community.document_loaders import WebBaseLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model = "meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

url = "https://docs.langchain.com/oss/python/langchain/overview"
loader = WebBaseLoader(url)

docs = loader.load()

prompt = PromptTemplate(
    template='Answer the following questions\n {question}\n based ont followiing text\n {text}',
    input_variables=['question','text']
    
)

chain = prompt | model | parser

result = chain.invoke({'question': 'What is langchain?','text': docs[0].page_content})

print(result)