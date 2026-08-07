# Todo API

一个简单的 Flask Todo 示例服务，用于演示代码审查流程。

## 运行

```bash
pip install -r requirements.txt
python app.py
```

## 接口

- `GET /api/search?q=xxx` 搜索用户
- `GET /api/todos` 列出当前用户的 todo（需 `Authorization: Bearer <token>`）
- `POST /api/todo` 新增 todo
