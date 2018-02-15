#!/bin/bash
python manage.py migrate
gunicorn userservice.wsgi:application -b :80