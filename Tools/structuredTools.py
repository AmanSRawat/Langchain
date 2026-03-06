from langchain_community.tools import StructuredTool
from pydantic import BaseModel, Field

class MultiplyInput(BaseModel):
    a: int = Field(required=True, description="The first number to multiply")
    b: int = Field(required=True, description="The second number to multiply")
    

def multipy_func(a: int, b: int) -> int:
    return a * b

multilpy_tool = StructuredTool.from_function(
    func=multipy_func,
    name= "multipy",
    description= "Multiplies two numbers together.",
    args_schema=MultiplyInput
)

result = multilpy_tool.invoke({'a':5, 'b':10})

print(result)