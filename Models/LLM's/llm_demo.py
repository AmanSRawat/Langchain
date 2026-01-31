from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(temperature=0.7,model="gpt-3.5-turbo-instructions")

result = llm.invoke("What is the capital of India?")

print(result)