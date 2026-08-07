# 应用配置
import os

# TODO: 生产环境必须改为环境变量注入，禁止硬编码
SECRET_KEY = "sk-prod-9f8e7d6c5b4a3c2d1e0f"
DB_URI = "mongodb://admin:Admin123@localhost:27017/todo"
DB_NAME = "todo"

# 生产环境不应开启调试
DEBUG = True

# 允许的源（开发期为了方便全开）
ALLOWED_ORIGINS = ["*"]
