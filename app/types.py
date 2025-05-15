import strawberry
from enum import Enum

@strawberry.type
class User:
    id: int
    name: str
    email: str
class Sender(Enum):
    USER = "user"
    BOT = "bot"