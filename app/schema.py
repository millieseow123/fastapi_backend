import strawberry
from .types import User
from .constants import mock_users
from .claude_client import get_chat_completion

@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> list[User]:
        return mock_users

    @strawberry.field
    def generate_chat_title(self, message: str) -> str:
        title_prompt = (
            f'Summarize this message into a short and clear chat title:\n"{message}"\n'
            "Return only the title without quotes."
        )
        return get_chat_completion(title_prompt)
    
    @strawberry.field
    def generate_ai_response(self, prompt: str) -> str:
        try:
            print("Prompt received:", prompt)
            response = get_chat_completion(prompt)
            print("Final response from get_chat_completion:", response)
            return response
        except Exception as e:
            print("ERROR in generate_ai_response:", str(e))
            return "Error: " + str(e)
        