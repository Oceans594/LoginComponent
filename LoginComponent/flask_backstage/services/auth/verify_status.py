# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:16
# @Site    :
# @File    : verify_status.py
from functools import wraps
from flask import session, request


def check_status(func):
    @wraps(func)
    def check_login(*args, **kwargs):
        if session.get('DY_Token') and request.cookies.get('dy_token'):
            return func(*args, **kwargs)
        else:
            return {'error': 'token已过期，请重新登录'}
    return check_login
