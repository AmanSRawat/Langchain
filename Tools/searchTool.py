from langchain_community.tools import DuckDuckGoSearchRun

search = DuckDuckGoSearchRun()

result = search.invoke("Today news over the iran vs iseral issue and its consequene on the indain market?")

print(result)