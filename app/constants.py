from .types import User
from datetime import datetime, timedelta
from .types import Sender

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

def current_iso_datetime():
    return datetime.now().isoformat(timespec="seconds")
def yesterday_iso_datetime():
    return (datetime.now() - timedelta(days=1)).isoformat(timespec="seconds")


mock_history = [
      {
        "id": "1",
        "title": "Follow-up reply",
        "createdAt": current_iso_datetime(),
        "messages": [
            {
                "sender": Sender.USER.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {"text": "How to respond if boss says no?"}
                        ]
                    }
                ]
            },
            {
                "sender": Sender.BOT.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {"text": "You can respond politely by saying: \"I understand your decision, and I appreciate your consideration. If there’s any way to revisit this request in the future, please let me know.\""}
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "2",
        "title": "Draft email for leave",
        "createdAt": yesterday_iso_datetime(),
        "messages": [
            {
                "sender": Sender.USER.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {"text": "Can you write an email requesting for leave?"}
                        ]
                    }
                ]
            },
            {
                "sender": Sender.BOT.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {
                                "text": "Sure, I’ve updated the email. Here’s the revised draft:\nSubject: Request for Leave\nDear [Manager’s Name],\nI hope this email finds you well. I am writing to formally request leave from [start date] to [end date] due to medical reasons.\nI will ensure that all my responsibilities are handled before my leave, and I am happy to assist in any transition or handover process required.\nThank you for considering my request. Please let me know if you need any additional information.\nBest regards,\n[Your Name]"
                            }
                        ]
                    }
                ]
            },
            {
                "sender": Sender.USER.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {"text": "Can you change the reason to \"medical reasons\"?"}
                        ]
                    }
                ]
            },
            {
                "sender": Sender.BOT.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {
                                "text": "Sure, I’ve updated the email. Here’s the revised draft:\nSubject: Request for Leave\nDear [Manager’s Name],\nI hope this email finds you well. I am writing to formally request leave from [start date] to [end date] due to medical reasons.\nI will ensure that all my responsibilities are handled before my leave, and I am happy to assist in any transition or handover process required.\nThank you for considering my request. Please let me know if you need any additional information.\nBest regards,\n[Your Name]"
                            }
                        ]
                    }
                ]
            }
        ]
    },
    {
        "id": "3",
        "title": "Weekly report summary",
        "createdAt": "2024-05-08T10:00:00",
        "messages": [
            {
                "sender": Sender.USER.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {"text": "Can you summarize this week’s report?"}
                        ]
                    }
                ]
            },
            {
                "sender": Sender.BOT.value,
                "text": [
                    {
                        "type": "paragraph",
                        "children": [
                            {
                                "text": "Here is the summary of this week’s report:\n1. Project A: Completed the initial phase and delivered the first draft to the client.\n2. Team B: Resolved 95% of the reported bugs and improved system performance by 20%.\n3. Upcoming Tasks: Finalize the budget for Project C and prepare for the client presentation next week."
                            }
                        ]
                    }
                ]
            }
        ]
    }
]
