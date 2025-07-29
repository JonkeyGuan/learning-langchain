# from langchain_openai.chat_models import ChatOpenAI
from langchain_core.messages import HumanMessage

from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# model = ChatOpenAI()
prompt = [HumanMessage("What is the capital of France?")]

response = model.invoke(prompt)
print(response.content)
