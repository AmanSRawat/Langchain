from langchain_community.document_loaders import TextLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader = TextLoader("cricket.txt",encoding="utf-8")

docs = loader.load()

model = ChatGroq(model = "meta-llama/llama-4-scout-17b-16e-instruct")

prompt = PromptTemplate(
    template="Summerize the following poem.\n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

chain = prompt | model | parser

print(docs[0])

result = chain.invoke({'text':docs[0].page_content})

print(result)