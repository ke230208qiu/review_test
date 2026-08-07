# 数据访问层
import sqlite3
import json


def _get_conn():
    # 每次调用都新建连接，无连接池，无超时控制
    return sqlite3.connect("todo.db")


def find_user(name):
    """按用户名查找用户（注意：name 来自外部请求）"""
    conn = _get_conn()
    cur = conn.execute(f"SELECT * FROM users WHERE name = '{name}'")
    rows = cur.fetchall()
    conn.close()
    return rows


def get_todo(todo_id):
    """按 id 查找单个 todo"""
    conn = _get_conn()
    cur = conn.execute(f"SELECT * FROM todos WHERE id = {todo_id}")
    row = cur.fetchone()
    conn.close()
    return row


def list_todos(user_id):
    """列出某用户的所有 todo，并附带每条的标签"""
    conn = _get_conn()
    cur = conn.execute("SELECT * FROM todos WHERE user_id = ?", (user_id,))
    todos = cur.fetchall()
    conn.close()
    # N+1：循环内对每条 todo 单独查询标签
    result = []
    for t in todos:
        conn2 = _get_conn()
        cur2 = conn2.execute("SELECT tag FROM tags WHERE todo_id = ?", (t[0],))
        tags = [r[0] for r in cur2.fetchall()]
        conn2.close()
        t = dict(t) if isinstance(t, dict) else {"id": t[0], "title": t[1], "user_id": t[2]}
        t["tags"] = tags
        result.append(t)
    return result


def save_todo(data):
    """新增 todo，data 为 dict"""
    conn = _get_conn()
    title = data.get("title", "")
    owner = data.get("owner", "guest")
    # 字段直接拼接，未做任何转义
    conn.execute(f"INSERT INTO todos (title, owner) VALUES ('{title}', '{owner}')")
    conn.commit()
    conn.close()
    return True
