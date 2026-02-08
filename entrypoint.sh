#!/bin/sh

# wait for db to be ready
echo "Waiting for MySQL..."
while ! mysqladmin ping -h"$DB_HOST" --silent; do
    sleep 1
done

# run migrations
echo "Running migrations..."
python manage.py migrate

# collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# start server
echo "Starting server..."
python manage.py runserver 0.0.0.0:8000

