# -*- coding: utf-8 -*-

"""
.. module:: {{PROJECT_NAME}}.auth.models
   :synopsis: User authentication models
"""

from flask.ext.security import RoleMixin, UserMixin
from {{PROJECT_NAME}}.models import BaseModel
from {{PROJECT_NAME}}.ext import db
from sqlalchemy.dialects import postgresql


class User(BaseModel, UserMixin):

    __tablename__ = 'auth_user'

    # Primary Key
    id = db.Column(db.Integer, primary_key=True)

    # Credentials
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))

    # Site Administrator
    super_user = db.Column(db.Boolean(), default=False)

    # User status
    active = db.Column(db.Boolean(), default=False)

    # Tracking
    confirmed_at = db.Column(db.DateTime())
    last_login_at = db.Column(db.DateTime())
    current_login_at = db.Column(db.DateTime())
    last_login_ip = db.Column(postgresql.INET)
    current_login_ip = db.Column(postgresql.INET)
    login_count = db.Column(db.Integer())

    # Relations
    roles = db.relationship(
        'Role',
        secondary='auth_user_roles',
        backref=db.backref('users', lazy='dynamic'))


class Role(BaseModel, RoleMixin):

    __tablename__ = 'auth_role'

    # Primary key
    id = db.Column(db.Integer(), primary_key=True)

    # Details
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))


class UserRoles(db.Model):

    __tablename__ = 'auth_user_roles'

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), primary_key=True)
