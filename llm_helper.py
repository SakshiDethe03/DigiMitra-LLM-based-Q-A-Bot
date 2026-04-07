from langchain_openai import ChatOpenAI
import os
api_key = os.getenv("OPENROUTER_API_KEY")

llm = ChatOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    model="openai/gpt-oss-120b:free",
)

if __name__ == "__main__":
    question = input("What is the question? ")
    response = llm.invoke(question)
    print(response.content)
