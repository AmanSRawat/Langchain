from langchain_community.tools import DuckDuckGoSearchRun
from langchain_core.tools import tool
from dotenv import load_dotenv
from langchain_classic.agents import create_react_agent
from langchain_classic.agents import AgentExecutor
from langchain_classic import hub
import requests
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

search_tool = DuckDuckGoSearchRun()

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools=[search_tool],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool],
    verbose=True
)

response = agent_executor.invoke({"input": "Tell me about the tension in the middle east and latest news on it?"})

print(response)
