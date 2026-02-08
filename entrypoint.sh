# #!/bin/sh
# set -e

# echo "Waiting for database..."
# until nc -z "$DB_HOST" "$DB_PORT"; do
#   sleep 1
# done
# echo "Database is ready"

# python manage.py migrate --noinput
# python manage.py collectstatic --noinput

# exec "$@"
#!/bin/sh
set -e

echo "Running migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Starting server..."
exec "$@"
