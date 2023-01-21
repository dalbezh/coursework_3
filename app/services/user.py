import base64
import hashlib
import hmac

from app.constants import PWD_HASH_SALT, PWD_HASH_ITERATIONS
from app.dao.user import UserDAO


class UserService:
    def __init__(self, dao: UserDAO):
        self.dao = dao

    def get_one(self, id):
        return self.dao.get_one(id)

    def get_by_email(self, email):
        return self.dao.get_by_email(email)

    def get_all(self):
        return self.dao.get_all()

    def create(self, data):
        password = data.get("password")
        data["password"] = self.password_hashing(password)
        return self.dao.create(data)

    def update(self, data):
        user = self.dao.get_one(data.get("id"))
        if "email" in data:
            user.email = data.get("email")
        if "name" in data:
            user.name = data.get("name")
        if "surname" in data:
            user.surname = data.get("surname")
        if "favorite_genre" in data:
            user.favorite_genre = data.get("favorite_genre")
        self.dao.update(user)

    def update_password(self, data):
        """
        Обновление пароля.
        Выведен в отдельный метод, чтобы нельзя было
        обновить пароль через HTTP метод PATCH
        """
        user = self.dao.get_one(data.get("id"))
        if "password" in data:
            user.password = data.get("password")
        self.dao.update(user)

    def delete(self, id):
        self.dao.delete(id)

    def password_hashing(self, password):
        """
        Хеширование пароля
        :param password: строка с паролем из запроса
        :return: хеш пароля
        """
        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return base64.b64encode(hash_digest)

    def compare_passwords(self, password_hash, other_password) -> bool:
        """
        Сравнение хэшей паролей
        :param password_hash: пароль из БД
        :param other_password: пароль из запроса
        :return: bool
        """
        decoded_digest = base64.b64decode(password_hash)

        hash_digest = hashlib.pbkdf2_hmac(
            'sha256',
            other_password.encode('utf-8'),
            PWD_HASH_SALT,
            PWD_HASH_ITERATIONS
        )

        return hmac.compare_digest(decoded_digest, hash_digest)
