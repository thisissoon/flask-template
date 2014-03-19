Using this Template
===================

*DELETE THIS AFTER THE TEMPLATE HAS BEEN PROCESSED*

This template is designed to be used with `Facio
<https://facio.readthedocs.org>`_. To use this template follow these commands:

.. code::

    sudo pip install facio
    facio foo --template git+git@github.com:thisissoon/flask-template.git
    mkvirtualenv foo --no-site-packages
    workon foo
    cd foo

{{PROJECT_NAME}}
================

# TODO: Project Blurb

Installing
----------

To install create a pythin virtual environment and run `make develop`.

.. code::

    mkvirtualenv {{PROJECT_NAME}} --no-site-packages
    workon {{PROJECT_NAME}}
    make develop

Running
-------

You need to expose a `SQLALCHEMY_DATABASE_URI` environment variable which
contains a url to your database url, for example:

.. code::

    postgres://root@localhost:5432/{{ PROJECT_NAME }}

This can be done in a `.env` file and activated using `Autoenv
<https://github.com/kennethreitz/autoenv>`_.

You can run the application calling the following make command:

.. code::

    make runserver

Database Migrations
-------------------

Exposing models
~~~~~~~~~~~~~~~

Database migrations are handled by `alembic`. To expose models to the
`alemvic` environment you need to add the module to the BLUEPRINTS list in
the config, for example:

.. code::

    BLUEPRINTS = [
        '{{PROJECT_NAME}}.auth',
    ]


Generating migrations
~~~~~~~~~~~~~~~~~~~~~

If the `migrations` directory does not exist you will need to run:

.. code::

    make db-init

You can then run the migrate command:

.. code::

    make db-migrate


Running Migrations
~~~~~~~~~~~~~~~~~~

To apply migrations just run the upgrade command:

.. code::

    make db-upgrade

Documentation Generation
------------------------

Documentation cna be generated bu running the following make command:

.. code::

    make docs-make

You can also view the docs by running:

.. code::

    make docs-serve

This will open the docs in your systems default browser in a new tab / window.

Credits
-------

Made by `SOON_ <http://thisissoon.com>`_. with paint brushes.
