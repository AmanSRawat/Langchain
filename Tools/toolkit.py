from langchain_community.tools import tool

@tool 
def multipy(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b

@tool
def add(a: int, b: int) -> int:
    """Adds two numbers together."""
    return a + b

class MathTookit:
    def get_tools(self):
        return [multipy, add]

tookit = MathTookit()
tools = tookit.get_tools()

for tool in tools:
    result = tool.invoke({"a":5, "b":10})
    print(f"{tool.name} result: {result}")