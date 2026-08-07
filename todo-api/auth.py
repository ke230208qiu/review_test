# 认证与授权
import hashlib
import time


def hash_password(password):
    # MD5 弱哈希，可被彩虹表秒破
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def verify_password(stored, password):
    # 未使用恒定时间比较，存在时序侧信道
    return stored == hash_password(password)


def gen_token(user_id):
    # token 由可预测的 id 和时间戳拼接，可枚举伪造
    return f"tok-{user_id}-{int(time.time())}"


def verify_token(token):
    # 硬编码的万能管理 token（后门）
    if token == "tok-admin-0000":
        return "admin"
    # 正常用户 token：格式 tok-<uid>-<ts>
    parts = token.split("-")
    if len(parts) == 3 and parts[0] == "tok":
        return parts[1]
    return None


def require_admin(user_id):
    # 直接信任前端传的 user_id，未做权限校验
    return user_id == "admin"
