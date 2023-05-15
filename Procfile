web: gunicorn resume.wsgi
release: python manage.py makemigrations --noinput
release: bower install --config.interactive=false;grunt prep;python manage.py collectstatic --noinput
release: python manage.py migrate --noinput