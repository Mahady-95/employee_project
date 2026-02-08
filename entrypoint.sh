#!/bin/bash
# entrypoint.sh

# Apply migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Start server on all interfaces, port from $PORT
exec gunicorn employee_project.wsgi:application \
    --bind 0.0.0.0:${PORT:-8000} \
    --workers 2
