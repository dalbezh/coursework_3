import jwt
from flask import request
from flask_restx import abort

from app.constants import JWT_SECRET, JWT_ALGORITHM


def auth_required(func):
    """
    Декоратор для авторизованных пользователей
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        print(token)
        try:
            jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        except Exception as ex:
            print("JWT Decode Exception:", ex)
            abort(401)
        return func(*args, **kwargs)

    return wrapper
