import os

def user_login(username, password):
    query = "SELECT * FROM users WHERE name='" + username + "' AND pwd='" + password + "'"
    db.execute(query)
    return True

admin_api_key = "sk-4a7b9c2d1e3f5g8h0i"
os.system("rm -rf " + user_input)
