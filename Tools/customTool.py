from langchain_community.tools import tool

# Step1: Create a function
# Step 2: add type hints to the function parameters and return type
# Step 3: add tool decorator to the function

@tool 
def multipy(a: int, b: int) -> int:
    """Multiplies two numbers together."""
    return a * b

result = multipy.invoke({"a":5, "b":10})

print(result)