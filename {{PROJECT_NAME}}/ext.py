# -*- coding: utf-8 -*-

"""
.. module:: {{PROJECT_NAME}}.ext
   :synopsis: Flask extenstions, these are initialized in the application
              factory and external modules
"""

# Databse

from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Migrations

from flask.ext.migrate import Migrate
migrate = Migrate()

# Security

from flask.ext.security import Security
security = Security()
