from langchain_text_splitters import RecursiveCharacterTextSplitter,Language

text = """
class Dog:
   
species = "canine" # A class attribute shared by all instances

def __init__(self, name, age):
    self.name = name  # Instance attribute, unique to each dog object
    self.age = age    # Instance attribute, unique to each dog object
    print(f"A new dog named {self.name} has been created!")

def bark(self):
    return f"{self.name} says"
    
dog1 = Dog("Buddy", 3)

# Access attributes and call methods using the object
print(f"Dog 1 Name: {dog1.name}")
print(f"Dog 1 Age: {dog1.age}")
print(f"Dog 1 Species: {dog1.species}")
print(dog1.bark())

# Create another object of the same class
dog2 = Dog("Max", 5)
print(f"Dog 2 Name: {dog2.name}")
print(dog2.bark()) 
"""

spliter = RecursiveCharacterTextSplitter.from_language(
    language = Language.PYTHON,
    chunk_size = 450,
    chunk_overlap = 0
)

chunks = spliter.split_text(text=text)

print(len(chunks))

print(chunks[0])