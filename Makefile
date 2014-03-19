#
# Makefile
#

clean_pyc:
	find . -name \*.pyc -delete

install:
	bash -c 'pip install -e .'

develop:
	bash -c 'pip install -e .[develop]'

test:
	bash -c 'pip install -e .[test]'
	python setup.py test

# Convenience methods

db-init:
	python ./manage.py db init

db-migrate:
	python ./manage.py db migrate

db-upgrade:
	python ./manage.py db upgrade

runserver:
	python ./manage.py server

# Documentaion Helpers

docs-make:
	make -C docs clean
	make -C docs html

docs-serve: docs-make
	cd docs/build/html; open "http://localhost:8000" && python -m SimpleHTTPServer
