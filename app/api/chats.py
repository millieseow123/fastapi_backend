from fastapi import APIRouter
from app.constants import mock_history

router = APIRouter()

@router.get("/chats")
def get_mock_chats():
    return mock_history
