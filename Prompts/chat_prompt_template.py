from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain is simple terms, what is {topic}?'),
    
])

prompt = chat_template.invoke({'domain': 'Cricket', 'topic': 'Virat Kohli'})

print(prompt)
