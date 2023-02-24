#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Running Entrypoint script....'
python manage.py wait_for_db
python manage.py makemigrations
python manage.py migrate
python manage.py auto_add_superuser
python manage.py collectstatic --noinput
# Normal Server
python manage.py runserver 0.0.0.0:8000
# or for enhanced local server
#python manage.py runserver_plus --keep-meta-shutdown 0.0.0.0:8000
