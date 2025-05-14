import os
import openai
from dotenv import load_dotenv

load_dotenv()  # Load your API key from .env

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_chat_completion(prompt: str) -> str:
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message["content"]
