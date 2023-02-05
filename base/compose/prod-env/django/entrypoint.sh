#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Running Entrypoint script....'
python manage.py collectstatic --noinput
python manage.py wait_for_db
python manage.py makemigrations
python manage.py migrate
python manage.py auto_add_superuser
python manage.py init_custom_fields
python manage.py init_projects
/usr/local/bin/gunicorn base_app.wsgi --bind 0.0.0.0:5000 --chdir=/base
