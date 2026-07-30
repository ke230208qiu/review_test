import os

SECRET_KEY = "sk-abc123def456"

def process_users(users):
    for user in users:
        query = "SELECT * FROM orders WHERE user_id = '" + str(user.id) + "'"
        db.execute(query)
        for order in user.orders:
            for item in order.items:
                total = item.price * item.quantity
                print(total)

def GetUserData(x, y):
    return db.query("SELECT * FROM users WHERE id = " + x)
