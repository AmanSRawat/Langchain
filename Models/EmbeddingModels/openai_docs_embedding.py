from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

document = [
    "Delhi is the capital of India.",
    "The capital of France is Paris.",
    "Berlin is the capital of Germany.",
    "Tokyo is the capital of Japan.",    
]

result = embeddings.embed_documents(document)

print(str(result))