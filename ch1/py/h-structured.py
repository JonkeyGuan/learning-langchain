# from langchain_openai import ChatOpenAI
from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

class AnswerWithJustification(BaseModel):
    """An answer to the user's question along with justification for the answer."""

    answer: str
    """The answer to the user's question"""
    justification: str
    """Justification for the answer"""


# llm = ChatOpenAI(model="gpt-3.5", temperature=0)
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0)

structured_llm = llm.with_structured_output(AnswerWithJustification)

response = structured_llm.invoke(
    "What weighs more, a pound of bricks or a pound of feathers")
print(response)
