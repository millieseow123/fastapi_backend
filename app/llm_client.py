import requests
import os
from dotenv import load_dotenv

from app.system_prompt import SYSTEM_PROMPT

load_dotenv()
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

def get_chat_completion(prompt: str) -> str:
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "HTTP-Referer": "http://localhost:3000",  
        "X-Title": "Schedulo",         
        "Content-Type": "application/json",
    }

    body = {
        "model": "openai/gpt-4.1",
        "messages": [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},    
        ],
        "max_tokens": 1000 
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=body, headers=headers)

    try:
        data = response.json()

    except Exception as e:
        return f"Error: Unable to parse JSON - {str(e)}"

    if response.status_code != 200:
        return f"Error: {response.status_code} - {data.get('error', {}).get('message', 'Unknown error')}"

    return data['choices'][0]['message']['content']
