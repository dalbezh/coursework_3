from flask import request
from flask_restx import Namespace, Resource

from app.container import user_service
from app.dao.model.user import UserSchema
from app.decorators import auth_required

user_ns = Namespace('user')

user_schema = UserSchema()


@user_ns.route('/<int:id>')
@user_ns.doc(params={'id': 'ID пользователя'},
             responses={
                 200: 'Success',
                 404: 'No data',
             }
             )
class UserViews(Resource):
    @auth_required
    def get(self, id: int):
        """
        Выдаёт пользователя по id
        """
        try:
            user = user_service.get_one(id)
            return user_schema.dump(user), 200
        except Exception as ex:
            return str(ex), 404

    @auth_required
    @user_ns.response(201, "Updated")
    def patch(self, id: int):
        """
        Обновление данных пользователя
        """
        data = request.json
        data["id"] = id
        user_service.update(data)
        return "", 201


@user_ns.route('/password')
@user_ns.doc(responses={
                 201: 'Password updated',
                 400: 'Bad Request (passwords do not match)',
             }
             )
class UserPasswordViews(Resource):
    @auth_required
    def put(self):
        """
        Обновление пароля пользователя
        """
        data = request.json

        email = data.get("email")
        old_password = data.get("old_password")
        new_password = data.get("new_password")

        user = user_service.get_by_email(email)

        if user_service.compare_passwords(user.password, old_password):
            user.password = user_service.password_hashing(new_password)
            result = user_schema.dump(user)
            user_service.update_password(result)
        else:
            return "", 400

        return "", 201
