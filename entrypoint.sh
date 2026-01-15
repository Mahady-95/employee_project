#!/bin/bash
set -e

echo "⏳ Waiting for MySQL..."

while ! mysqladmin ping -h "$DB_HOST" -u"$DB_USER" -p"$DB_PASSWORD" --silent; do
    sleep 2
done

echo "✅ MySQL is up - starting Django"

python manage.py migrate
exec python manage.py runserver 0.0.0.0:8000
