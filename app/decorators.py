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


def admin_required(func):
    """
    Декоратор для авторизации администраторов
    """
    def wrapper(*args, **kwargs):
        if 'Authorization' not in request.headers:
            abort(401)

        data = request.headers['Authorization']
        token = data.split("Bearer ")[-1]
        role = None
        try:
            user = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
            role = user.get('role', 'user')
        except Exception as ex:
            print("JWT Decode Exception:", ex)
            abort(401)

        if role != 'admin':
            abort(403)  # Forbidden

        return func(*args, **kwargs)

    return wrapper
