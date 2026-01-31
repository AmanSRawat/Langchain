from langchain import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name="gpt-4")

result = model.invoke("What is the capital of India?")

print(result.content)