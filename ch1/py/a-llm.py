# from langchain_openai.chat_models import ChatOpenAI

# model = ChatOpenAI(model="gpt-3.5-turbo")

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

response = model.invoke("The sky is")
print(response.content)

