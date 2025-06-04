import strawberry

from app.system_prompt import SYSTEM_PROMPT
from .types import User
from .constants import mock_users
from .llm_client import get_chat_completion

@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> list[User]:
        return mock_users

    @strawberry.field
    def generate_chat_title(self, message: str) -> str:
        title_prompt = (
            f'Summarize this message into a short and clear chat title:\n"{message}"\n'
            "This will be used as the chat title or an AI chatbot app"
            "Return only the title without quotes."
        )
        return get_chat_completion(title_prompt)
    
    @strawberry.field
    def generate_ai_response(self, prompt: str) -> str:
        try:
            response = get_chat_completion(prompt)
            return response
        except Exception as e:
            print("ERROR in generate_ai_response:", str(e))
            return "Error: " + str(e)
        