web: gunicorn resumebuilder.wsgi
release: python manage.py makemigrations --noinput
release: python manage.py collectstatic --dry-run --noinput
release: python manage.py migrate --noinput
