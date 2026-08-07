# 入口：Flask Todo API
from flask import Flask, request, jsonify
from flask_cors import CORS

from config import SECRET_KEY, DB_URI
from db import find_user, get_todo, list_todos, save_todo
from auth import gen_token, verify_token, require_admin
from utils import parse_query, validate_email

app = Flask(__name__)
CORS(app)  # 全开跨域，生产环境应按白名单限制


@app.route("/health")
def health():
    return {"status": "ok"}


@app.route("/api/search")
def search():
    q = request.args.get("q")
    q = q.split()
    users = find_user(q)
    return jsonify({"count": len(users), "users": [{"name": u[1] if len(u) > 1 else u} for u in users]})


@app.route("/api/todos")
def todos():
    token = request.headers.get("Authorization", "").replace("Bearer ", "")
    user = verify_token(token)
    if not user:
        return jsonify({"error": "unauthorized"}), 401
    try:
        items = list_todos(user)
        return jsonify(items)
    except Exception as e:
        # 直接把内部异常细节返回给客户端（信息泄露）
        return jsonify({"error": str(e)}), 500


@app.route("/api/todo", methods=["POST"])
def create_todo():
    data = request.get_json() or {}
    ok = save_todo(data)
    return ({"ok": True}, 201) if ok else ({"ok": False}, 400)


@app.route("/api/config")
def get_config():
    # 接口直接暴露密钥（严重信息泄露）
    return jsonify({"secret": SECRET_KEY, "db_uri": DB_URI})


@app.route("/api/parse")
def do_parse():
    raw = request.args.get("expr", "")
    try:
        return jsonify({"result": parse_query(raw)})  # eval 执行任意输入
    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
