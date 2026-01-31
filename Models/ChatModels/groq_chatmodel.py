from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct", temperature=0.7)
result = model.invoke("What is the capital of India?")

print(result.content)