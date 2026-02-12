from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGroq(model = 'meta-llama/llama-4-scout-17b-16e-instruct')

parser = StrOutputParser()

class Feedback(BaseModel):
    sentiment: Literal['positive','negative'] = Field(description='Give sentiment of the feedback')
    
parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the feedback as positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables= {'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template= 'Generate the appropriate respose for the positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Genrate the appropriate response for the negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment=='positive', prompt2 | model | parser),
    (lambda x: x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "coundnot find sentiment")
)

chain = classifier_chain | branch_chain

result = chain.invoke({'feedback': 'This is a wonderful phone!'})

print(result)

chain.get_graph().print_ascii()