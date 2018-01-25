#!/bin/bash -xe

echo secret key test: $SECRET_KEY
python /usr/src/app/manage.py collectstatic --noinput
gunicorn ui.wsgi --bind 0.0.0.0:$PORT --log-file -
