# ==============================
# Base Image
# ==============================
FROM python:3.10-slim

# ==============================
# Python settings
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# ==============================
# Set working directory
# ==============================
WORKDIR /app

# ==============================
# Install OS dependencies for your requirements
# ==============================
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    libffi-dev \
    libjpeg-dev \
    zlib1g-dev \
    libfreetype6-dev \
    libxml2-dev \
    libxslt1-dev \
    libcairo2-dev \
    pkg-config \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Copy requirements.txt first (for caching)
# ==============================
COPY requirements.txt .

# ==============================
# Upgrade pip & install Python deps
# ==============================
RUN pip install --upgrade pip setuptools wheel Cython \
    && pip install --no-cache-dir -r requirements.txt

# ==============================
# Copy project files
# ==============================
COPY . .

# ==============================
# Expose port (adjust if needed)
# ==============================
EXPOSE 8000

# ==============================
# Default command
# ==============================
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
