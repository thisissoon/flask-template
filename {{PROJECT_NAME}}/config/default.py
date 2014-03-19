# -*- coding: utf-8 -*-

"""
.. module:: {{PROJECT_NAME}}.config.default
   :synopsis: Default configuration for Flask, do not use for Production
"""

import os

# Debug

DEBUG = True

# Security

SECRET_KEY = 'changeme'
SECURITY_TRACKABLE = True
SECURITY_PASSWORD_HASH = 'sha512_crypt'
SECURITY_PASSWORD_SALT = SECRET_KEY

# Database

DEFAULT_DATABASE_URI = 'sqlite://:memory:'
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or \
    DEFAULT_DATABASE_URI

# Blueprints

BLUEPRINTS = [
    '{{PROJECT_NAME}}.auth',
]
