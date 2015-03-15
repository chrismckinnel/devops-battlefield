.PHONY: install remove_media remove_pyc update_virtualenv remove_db create_db load_fixtures

build: remove_pyc update_virtualenv create_db

install: remove_media remove_pyc update_virtualenv create_db load_fixtures migrate collectstatic

remove_media:
	-rm -rf public/media/*

remove_pyc:
	-find . -type f -name "*.pyc" -exec rm -rf {} \;

update_virtualenv:
	cd /tmp && pip install -r requirements.txt

create_db:
	python manage.py syncdb --noinput

migrate:
	python manage.py migrate

load_fixtures:
	python manage.py loaddata fixtures/*.json

collectstatic:
	python manage.py collectstatic --noinput

test:
	runtests.sh

ci: update_virtualenv test
