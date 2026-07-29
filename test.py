import os

def login(username, password):
    query = f"SELECT * FROM users WHERE name='{username}' AND pwd='{password}'"
    db.execute(query)

api_key = "sk-abc123def456ghi789jkl"

def get_user(user_id):
    return users[int(user_id)]
