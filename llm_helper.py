from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    model="openai/gpt-oss-120b:free",
)

if __name__ == "__main__":
    question = input("What is the question? ")
    response = llm.invoke(question)
    print(response.content)