import strawberry
from .types import User

mock_users = [
    User(id='1', name='Alice Johnson', email='alice.johnson@example.com'),
    User(id='2', name='Bob Smith', email='bob.smith@example.com'),
    User(id='3', name='Charlie Chen', email='charlie.chen@example.com'),
    User(id='4', name='Dana Lee', email='dana.lee@example.com'),
    User(id='5', name='Ethan Park', email='ethan.park@example.com'),
    User(id='6', name='Fiona Davis', email='fiona.davis@example.com'),
    User(id='7', name='George Wu', email='george.wu@example.com'),
    User(id='8', name='Hannah Kim', email='hannah.kim@example.com'),
    User(id='9', name='Ian Patel', email='ian.patel@example.com'),
    User(id='10', name='Julia Wong', email='julia.wong@example.com'),
    User(id='11', name='Kevin Garcia', email='kevin.garcia@example.com'),
    User(id='12', name='Lily Zhang', email='lily.zhang@example.com'),
    User(id='13', name='Mike Nguyen', email='mike.nguyen@example.com'),
    User(id='14', name='Nina Thompson', email='nina.thompson@example.com'),
    User(id='15', name='Oscar Rivera', email='oscar.rivera@example.com'),
    User(id='16', name='Paula Tan', email='paula.tan@example.com'),
    User(id='17', name='Quincy Adams', email='quincy.adams@example.com'),
    User(id='18', name='Rachel Lim', email='rachel.lim@example.com'),
    User(id='19', name='Samir Desai', email='samir.desai@example.com'),
    User(id='20', name='Tina Chua', email='tina.chua@example.com'),
]
@strawberry.type
class Query:
    @strawberry.field
    def get_users(self) -> list[User]:
        return mock_users

