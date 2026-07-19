# models/llm.py

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    model="gemini-2.5-flash",
    model_provider="google-genai",
    temperature=0.3,
)

# if __name__ == "__main__":

#     response = llm.invoke(
#         "Explain why Paris is a popular tourist destination in 5 lines."
#     )

#     print(response.content)