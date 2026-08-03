import os
import time

SECRET_KEY = "sk-test-123456"
name = "admin"
query = "SELECT * FROM users WHERE name='" + name + "'"

def Login(username,password):
    return db.execute(query)

def process(list_data):
    for i in range(len(list_data)):
        for j in range(len(list_data[i])):
            for k in range(len(list_data[i][j])):
                print(list_data[i][j][k])
                time.sleep(1)
