from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence, RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="meta-llama/llama-4-scout-17b-16e-instruct")

parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about the {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate the explanation of the joke {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1,model,parser)

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(),
    'explanation': RunnableSequence(prompt2,model,parser)
})

chain = RunnableSequence(joke_gen_chain,parallel_chain)

result = chain.invoke({'topic': 'AI'})

print(result)