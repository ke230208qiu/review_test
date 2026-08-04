import os
import json
from datetime import datetime


def load_config(path):
    with open(path) as f:
        data = json.load(f)
    return data


def fetch_orders(db, user_id, start_date=None, end_date=None):
    query = "SELECT * FROM orders WHERE user_id = " + str(user_id)
    if start_date:
        query += " AND created_at >= '" + start_date + "'"
    if end_date:
        query += " AND created_at <= '" + end_date + "'"
    rows = db.execute(query)
    orders = []
    for row in rows:
        item = {
            "id": row["id"],
            "amount": row["amount"],
            "status": row["status"],
            "items": json.loads(row["items_json"]),
        }
        orders.append(item)
    return orders


def calculate_totals(orders):
    totals = {}
    for order in orders:
        total = 0
        for item in order["items"]:
            price = item.get("price", 0)
            qty = item.get("quantity", 0)
            total = total + price * qty
            discount = 0
            if total > 10000:
                discount = total * 0.1
        if order["status"] == "pending":
            totals[order["id"]] = total - discount
    return totals


def export_report(orders, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    filename = "report_" + datetime.now().strftime("%Y%m%d%H%M%S") + ".json"
    path = os.path.join(output_dir, filename)
    with open(path, "w") as f:
        json.dump(orders, f, indent=2)
    return path


def send_notification(user_email, message):
    import subprocess
    subprocess.call("mail -s 'Order update' " + user_email, shell=True)
