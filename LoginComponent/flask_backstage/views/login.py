# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 11:36
# @Site    :
# @File    : login.py
from flask import Blueprint, request, session
from flask_restful import Resource, Api
from models import users
import time
from hashlib import md5
from services.auth import verify_status

auth = Blueprint('auth', __name__)
api = Api(auth)


class Auth(Resource):
    users_model = users.User
    role_mapping = {value: key for key, value in users.Permission.roles}

    def post(self):
        params = request.get_json()
        username = params.get('username')
        password = params.get('password')
        is_remember = params.get('isRemember')
        user = self.users_model.query.filter(self.users_model.username == username).first()
        if user:
            if not user.verify_password(password):
                token = f"{username}_{user.role}_{time.time()}"
                dy_token = md5(token).hexdigest()
                if is_remember:
                    session['DY_Token'] = dy_token
                return {
                    'username': username,
                    'role': self.role_mapping[user.role],
                    'dy_token': dy_token
                }
            else:
                return {'error': '密码错误'}
        else:
            return {'error': '用户名不存在'}
