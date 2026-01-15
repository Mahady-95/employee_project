FROM python:3.10-bullseye

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# system deps
# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-mysql-client \
    default-libmysqlclient-dev \
    gcc \
    python3-dev \
    netcat-openbsd \
 && rm -rf /var/lib/apt/lists/*

# pip
RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy project
COPY . .

# entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
