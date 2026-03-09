from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub
from dotenv import load_dotenv
import requests
load_dotenv()

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")
search_tool = DuckDuckGoSearchRun()

@tool
def get_weather_data(city: str) -> str:
  """
  This function fetches the current weather data for a given city
  """
  url = f'https://api.weatherstack.com/current?access_key=4d1d8ae207a8c845a52df8a67bf3623e&query={city}'

  response = requests.get(url)

  return response.json()

prompt = hub.pull("hwchase17/react")

agent = create_react_agent(
    llm=llm,
    tools = [search_tool, get_weather_data],
    prompt=prompt
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=[search_tool, get_weather_data],
    verbose=True
)

response = agent_executor.invoke({"input":"Whta is the capital of Uttarakhand and what is the current weather there?"})

print(response['output'])