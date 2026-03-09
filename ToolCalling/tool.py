from langchain_core.tools import tool
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage
from pydantic import BaseModel, Field # Add this import

load_dotenv()

# Define a schema for the tool inputs
class MultiplySchema(BaseModel):
    a: int = Field(description="The first integer")
    b: int = Field(description="The second integer")

llm = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

@tool(args_schema=MultiplySchema) # Link the schema here
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers a and b."""
    return a * b

llm_with_tool = llm.bind_tools([multiply])

query = HumanMessage(content="What is 5 multiplied by 10?")
messages = [query]

# This should now pass validation
result = llm_with_tool.invoke(messages)
messages.append(result)

tool_result = multiply.invoke(result.tool_calls[0])

messages.append(tool_result)
response = llm_with_tool.invoke(messages) 

print(response.content)