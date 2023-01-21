import datetime
import calendar
import jwt
from flask_restx import abort

from app.services.user import UserService
from app.constants import JWT_SECRET, JWT_ALGORITHM


class AuthService:
    def __init__(self, user_service: UserService):
        self.user_service = user_service

    def generate_tokens(self, email, password, is_refresh=False):
        """
        Генерация JWT
        :param email: почтовый ящик пользователя
        :param password: пароль пользователя (хэш)
        :param is_refresh: refresh_token
        :return: access_token и refresh_token
        """
        user = self.user_service.get_by_email(email)
        if user is None:
            abort(403)

        if not is_refresh:
            if not self.user_service.compare_passwords(user.password, password):
                abort(400)

        data = {
            "email": user.email,
        }

        # 30 min for access_token
        short_time = datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        data["exp"] = calendar.timegm(short_time.timetuple())
        access_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        # 130 days for refresh_token
        long_time = datetime.datetime.utcnow() + datetime.timedelta(days=130)
        data["exp"] = calendar.timegm(long_time.timetuple())
        refresh_token = jwt.encode(data, JWT_SECRET, algorithm=JWT_ALGORITHM)

        tokens = {
            "access_token": access_token,
            "refresh_token": refresh_token
        }

        return tokens

    def approve_refresh_token(self, refresh_token):
        """
        Проверяет refresh_token и если он не истек и валиден — генерирует пару access_token и refresh_token
        :param refresh_token: ранее выданный токен
        :return: access_token и refresh_token
        """
        data = jwt.decode(jwt=refresh_token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = data.get("email")
        if email is None:
            abort(403)
        user = self.user_service.get_by_email(email)

        return self.generate_tokens(email, user.password, is_refresh=True)

    def validate_tokens(self, access_token, refresh_token):
        """
        Проверяет валидность токенов
        :param access_token: access_token
        :param refresh_token: refresh_token
        :return: bool
        """
        for token in [access_token, refresh_token]:
            try:
                jwt.decode(jwt=token, key=JWT_SECRET, algorithms=[JWT_ALGORITHM])
            except Exception:
                return False

        return True
