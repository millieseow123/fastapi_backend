import strawberry
from .types import User
from .constants import mock_users
from openai_client import get_chat_completion

@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> list[User]:
        return mock_users

@strawberry.type
class Query:
    @strawberry.field
    def generate_ai_response(self, prompt: str) -> str:
        return get_chat_completion(prompt)