# -*- coding: utf-8 -*-

"""
.. module:: {{PROJECT_NAME}}.app
    :synopsis: Flask application factory pattern:
               http://flask.pocoo.org/docs/patterns/appfactories/
"""

import os

from flask import Flask
from flask.ext.security import SQLAlchemyUserDatastore
from {{PROJECT_NAME}}.auth.models import User, Role
from {{PROJECT_NAME}}.ext import db, migrate, security


def load_config(app, override=None):
    """
    Load application configuration from default module then overriding
    by environment variables

    :param app: Flask application instance
    :type app: flask.app.Flask
    """

    # Default configuration
    app.config.from_object('{{PROJECT_NAME}}.config.default')

    # Override using os environment variable
    if os.environ.get('{{PROJECT_NAME}}_SETTINGS_PATH'):
        app.config.from_envvar('{{PROJECT_NAME}}_SETTINGS_PATH')

    # If override path is supplied use those settings
    if override:
        app.config.from_pyfile(override)


def register_blueprints(app):
    """
    Load blueprints from config, similar to the INSALLED_APPS
    setting in Django

    :param app: Flask application instance
    :type app: flask.app.Flask
    """

    for blueprint in app.config['BLUEPRINTS']:

        # Register Blueprints
        try:
            module = __import__(
                '{0}'.format(blueprint),
                fromlist=['{{PROJECT_NAME}}'])
            app.register_blueprint(module.blueprint)
        except ImportError:
            # TODO: Warning here
            pass
        except AttributeError:
            # TODO: Warning here
            pass

        # Import models
        try:
            __import__('{0}.models'.format(blueprint))
        except ImportError:
            # TODO: Warning here
            pass


def register_extenstions(app):
    """
    Load flask extensions

    :param app: Flask application instance
    :type app: flask.app.Flask
    """

    # Database (Flask-SQLAlchemy)
    db.init_app(app)

    # Migrations
    migrate.init_app(app, db)

    # Flask Security
    datastore = SQLAlchemyUserDatastore(db, User, Role)
    security.init_app(app, datastore=datastore)


def create_app():
    """
    Bootstrap flask application
    """

    # Initialize Flask Application
    app = Flask(__name__)

    # Load Configuration
    load_config(app)

    # Initialize extensions
    register_extenstions(app)

    # Dynamically load blueprints
    register_blueprints(app)

    return app
