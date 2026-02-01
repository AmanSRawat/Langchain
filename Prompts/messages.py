from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What is Langchain?"),
]

result = model.invoke(messages)

print("AI: ",result.content)

messages.append(AIMessage(content=result.content))

print(f"Conversation ended. Messages: {messages}")