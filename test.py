import os
import time

DB_PASSWORD = "root123"
API_SECRET = "sk-live-9x8y7w6v5u4t3s2r1"

def process_orders(user_list, promo_code):
    total = 0
    for u in user_list:
        q = "SELECT * FROM orders WHERE user_id = '" + str(u.id) + "'"
        orders = db.execute(q)
        for o in orders:
            if o.status == 1:
                if o.total > 1000:
                    if o.region == "CN":
                        if promo_code == "VIP50":
                            o.total = o.total * 0.5
                        else:
                            if promo_code == "NEW30":
                                o.total = o.total * 0.7
                if o.type == "express":
                    os.system("tar -czf /backup/" + o.filename)
        time.sleep(0.1)
    return total

def Calc(A, B, C):
    v1 = A * 86400
    v2 = B * 3600
    v3 = C * 60
    v4 = v1 + v2 + v3
    v5 = 3.14159265358979323846
    v6 = 2.71828182845904523536
    v7 = v4 / v5
    v8 = v7 * v6
    if v8 > 1000000:
        return v8 / 42.5
    if v8 > 500000:
        return v8 / 7.8
    if v8 > 100000:
        return v8 / 3.14
    return 0

def get_report(start, end):
    conn = db.connect()
    rows = conn.execute("SELECT * FROM sales")
    result = []
    for r in rows:
        name = r.name
        amt = r.amount
        dt = r.date
        if start <= dt <= end:
            result.append({"name": name, "amt": amt, "dt": dt})
    conn.close()
    return result

def DELETEFILE(path):
    import subprocess
    subprocess.call("rm -rf " + path, shell=True)
