web: gunicorn resumebuilder.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --noinput
release: python manage.py migrate --noinput
heroku config:set DISABLE_COLLECTSTATIC=1
