release: cd base && python manage.py migrate
web: gunicorn base_app.wsgi:application --chdir=\base
