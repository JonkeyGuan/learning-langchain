from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer all questions to the best of         your ability."),
    ("placeholder", "{messages}"),
])

# model = ChatOpenAI()
model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

chain = prompt | model

response = chain.invoke({
    "messages": [
        ("human", "Translate this sentence from English to French: I love programming."),
        ("ai", "J'adore programmer."),
        ("human", "What did you just say?"),
    ],
})

print(response.content)
