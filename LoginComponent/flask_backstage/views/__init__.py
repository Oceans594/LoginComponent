# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 11:22
# @Site    :
# @File    : __init__.py.py
from flask import Flask
from flask_cors import CORS
from config import config
from views.login import Auth as auth_blueprint
from datetime import timedelta

app = Flask(__name__)
# 允许跨域请求
CORS(app, resources=r'/*')

# 注册蓝图
app.register_blueprint(auth_blueprint)

# 应用配置
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)
app.config['SQLALCHEMY_DATABASE_URI'] = config['mysql'].DATABASE_TEST_URI
app.secret_key = config['base'].SECRET_KEY


@app.before_first_request
def init():
    """
    请求之前创建root用户
    :return:
    """
    pass
