from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatGroq(model = "meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke on the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Give the explanation of the joke {text}',
    input_variables=['text']
)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)

result = chain.invoke({'topic':'AI'})

print(result)