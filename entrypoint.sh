#!/bin/bash
set -e

# Ensure line endings are LF
# 🟢 Important on Windows: run dos2unix entrypoint.sh before building

echo "⏳ Waiting for MySQL at $DB_HOST:$DB_PORT..."

# Wait for MySQL to be ready
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 2
done

echo "✅ MySQL is up. Running migrations..."

# Run migrations
python manage.py migrate --no-input

# Load positions fixture if exists
if [ -f employee_register/fixtures/positions.json ]; then
    echo "📂 Loading positions fixture..."
    python manage.py loaddata employee_register/fixtures/positions.json
fi

# Collect static files (optional)
python manage.py collectstatic --no-input 2>/dev/null || true

# Execute default CMD
exec "$@"
