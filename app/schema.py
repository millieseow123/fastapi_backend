import strawberry
from .resolvers import hello_resolver
from .types import Query

@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=hello_resolver)

schema = strawberry.Schema(query=Query)
