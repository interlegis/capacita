#!/bin/sh

migrate_things=$(python3 manage.py migrate --noinput 2>&1)

echo $migrate_things

start_server=$(python3 manage.py runserver 0.0.0.0:8000 2>&1)

echo $start_server