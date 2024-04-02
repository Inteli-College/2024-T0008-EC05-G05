from tinydb import TinyDB

# Create the database
db = TinyDB('user_activities.json')

logs_table = db.table('logs')

# Sample activities with dates incremented by two days, starting from 25/03/2024
activities = [
    {"user": "User 1", "activity": "editar", "kit": 1, "hour": "10:00", "date": "25/03/2024"},
    {"user": "User 2", "activity": "editar", "kit": 2, "hour": "11:00", "date": "27/03/2024"},
    {"user": "User 3", "activity": "editar", "kit": 3, "hour": "12:00", "date": "29/03/2024"},
    {"user": "User 4", "activity": "editar", "kit": 1, "hour": "13:00", "date": "31/03/2024"},
    {"user": "User 5", "activity": "editar", "kit": 2, "hour": "14:00", "date": "02/04/2024"},
    {"user": "User 6", "activity": "editar", "kit": 3, "hour": "15:00", "date": "04/04/2024"},
    {"user": "User 7", "activity": "editar", "kit": 1, "hour": "16:00", "date": "06/04/2024"},
]

logs_table.insert_multiple(activities)
