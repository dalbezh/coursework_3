from flask import request
from flask_restx import Namespace, Resource

from app.container import auth_service, user_service

auth_ns = Namespace('auth')


@auth_ns.route('/register')
@auth_ns.doc(responses={201: 'Successful registration',
                        400: 'Bad Request (incorrect input data)'})
class RegisterViews(Resource):
    def post(self):
        """
        Регистрация и получение токенов
        """
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return "", 400

        user_service.create(data)

        return "", 201


@auth_ns.route('/login')
@auth_ns.doc(responses={201: 'Updated access_token and refresh_token'})
class AuthsViews(Resource):
    @auth_ns.response(401, "Unauthorized")
    def post(self):
        """
        Аутентификация и получение токенов
        """
        data = request.json

        email = data.get("email", None)
        password = data.get("password", None)

        if None in [email, password]:
            return "401 Unauthorized", 401

        tokens = auth_service.generate_tokens(email, password)

        return tokens, 201

    @auth_ns.response(400, "Validated FAIL")
    def put(self):
        """
        Обновление токенов
        """
        data = request.json
        access_token = data.get("access_token")
        refresh_token = data.get("refresh_token")

        validated = auth_service.validate_tokens(access_token, refresh_token)

        if not validated:
            return "", 400

        tokens = auth_service.approve_refresh_token(refresh_token)

        return tokens, 201
