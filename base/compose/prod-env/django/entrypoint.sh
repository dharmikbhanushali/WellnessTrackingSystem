#!/bin/bash

set -o errexit
set -o pipefail
set -o nounset

echo 'Running Entrypoint/Post Build script....'
python manage.py collectstatic --noinput
python manage.py wait_for_db
python manage.py makemigrations
python manage.py migrate
python manage.py auto_add_superuser
#gunicorn base_app.wsgi --bind 0.0.0.0:8000 --chdir=base --access-logfile '-' --error-logfile '-' --timeout 600 --workers=4
# or
#gunicorn base_app.wsgi --bind 0.0.0.0:8000 --chdir=. --access-logfile '-' --error-logfile '-' --timeout 600 --workers=4
# or
# gunicorn base_app.wsgi --bind=0.0.0.0:8000 --timeout 60 --access-logfile '-' --error-logfile '-' -k uvicorn.workers.UvicornWorker --chdir=base --workers 8 --threads 4
