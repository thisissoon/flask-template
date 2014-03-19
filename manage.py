# -*- coding: utf-8 -*-
#!/usr/bin/env python

"""
.. module:: manage
   :synopsis: Flask manager for perfomining management commands such as
              running a local development server.
"""

import re
import sys

from flask.ext.migrate import Migrate, MigrateCommand
from flask.ext.script import Manager, prompt, prompt_pass, Shell, Server
from flask.ext.security import SQLAlchemyUserDatastore
from flask.ext.security.utils import encrypt_password
from {{ PROJECT_NAME }}.app import create_app
from {{ PROJECT_NAME }}.auth.models import User, Role
from {{ PROJECT_NAME }}.ext import db


app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)


EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")


def _make_context():
    """
    Return context dict for a shell session so you can access
    app, db, and the User model by default.
    """

    return {
        'app': app,
        'db': db,
        'User': User
    }


@manager.command
def schema_diagram():
    """
    Draw an Entity Relationship Diagram
    """

    from sqlalchemy_schemadisplay import create_schema_graph

    graph = create_schema_graph(
        metadata=db.MetaData(app.config['SQLALCHEMY_DATABASE_URI']),
        show_datatypes=True,
        show_indexes=True
    )

    graph.write_png('schema.png')


@manager.command
def createsuperuser():
    """
    Create a super user of the system, requiring Email and password.
    """

    email = prompt('User E-Mail')
    email_confirm = prompt('Confirm E-Mail')

    if not email == email_confirm:
        sys.exit('\nCould not create user: E-Mail did not match')

    if not EMAIL_REGEX.match(email):
        sys.exit('\nCould not create user: Invalid E-Mail addresss')

    password = prompt_pass('User password')
    password_confirm = prompt_pass('Confirmed password')

    if not password == password_confirm:
        sys.exit('\nCould not create user: Passwords did not match')

    datastore = SQLAlchemyUserDatastore(db, User, Role)
    datastore.create_user(
        email=email,
        password=encrypt_password(password),
        active=True,
        super_user=True)

    db.session.commit()


manager.add_command("server", Server())
manager.add_command('db', MigrateCommand)
manager.add_command("shell", Shell(make_context=_make_context))


if __name__ == "__main__":
    manager.run()
