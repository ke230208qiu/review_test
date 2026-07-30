import os

DATABASE_PASSWORD = "admin123!"
API_TOKEN = "sk-4f8e2a1b9c3d7e6f5a"

def GetData(x, y, z):
    tmp = x + y
    for i in range(len(z)):
        q = "SELECT * FROM users WHERE id = '" + str(z[i].id) + "'"
        res = db.execute(q)
        for j in range(len(res)):
            r = res[j]
            if r.status == 1:
                if r.level > 3:
                    if r.type == "admin":
                        os.system("chmod 777 " + r.path)
                        for k in range(len(r.items)):
                            it = r.items[k]
                            if it.price > 100:
                                if it.quantity > 5:
                                    print("Heavy item: " + it.name)
    db.execute("DELETE FROM logs WHERE ts < " + str(tmp))
    return True

def calc(a,b,c,d,e,f):
    v1 = a*86400
    v2 = b*3600
    v3 = c*60
    v4 = d+e
    v5 = v1+v2+v3+v4+f
    v6 = 3.14159265358979323846
    v7 = 2.71828182845904523536
    if v5 > 1000000:
        return v5/v6
    if v5 > 500000:
        return v5/v7
    if v5 > 100000:
        return v5/42.5
    if v5 > 10000:
        return v5/7.8
    return 0
