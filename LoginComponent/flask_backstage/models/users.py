# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 11:23
# @Site    :
# @File    : users.py
from flask_backstage.models import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


class Permission:
    """
    权限认证,基于Linux文件系统权限
    |   get   |   post   |   put   |    delete  |
    对应Restful规范
    """
    GET = 0b1000        # 查看
    POST = 0b0100       # 新增
    PUT = 0b0010        # 修改
    DELETE = 0b0001     # 删除
    roles = {
        'customer': bin(GET),
        'salesman': bin(GET + POST),
        'administrator': bin(GET + POST + PUT + DELETE)
    }


class User(db.Model):
    __tablename__ = "users"
    __table_args__ = {"mysql_charset": "utf8"}
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, index=True)  # 用户名
    password_hash = db.Column(db.String(256))  # 密码哈希值
    role = db.Column(db.Boolean, default=Permission.roles['customer'])  # 角色
    create_time = db.Column(db.DateTime, default=datetime.now)  # 创建时间
    description = db.Column(db.Text(100), default=None)  # 描述
    is_active = db.Column(db.Boolean, default=True)  # 是否启用

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    def set_user_role(self, role):
        self.role = Permission.roles[role.lower()]

    def __repr__(self):
        return f"<User {self.username}>"
