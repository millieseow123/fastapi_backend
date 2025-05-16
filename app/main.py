from fastapi import FastAPI
import strawberry
from strawberry.fastapi import GraphQLRouter
from app.schema import Query
from fastapi.middleware.cors import CORSMiddleware
from app.api.chats import router as chats_router

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema)

app = FastAPI()
app.include_router(graphql_app, prefix="/graphql")
app.include_router(chats_router, prefix="/api")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

