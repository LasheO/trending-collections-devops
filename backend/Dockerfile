# Backend Dockerfile
# 
# This file contains instructions for Docker to build a container image
# for the Flask backend application.
#
# Author: Lashe Onamusi
# Date: March 2026

# ==============================================================================
# STAGE 1: BASE IMAGE
# ==============================================================================
# Start from official Python 3.11 image (Alpine is smaller/faster)
FROM python:3.11-slim

# Set metadata labels (good practice for documentation)
LABEL maintainer="Lashe Onamusi"
LABEL description="Backend API for Trending Collections DevOps App"
LABEL version="1.0"

# ==============================================================================
# STAGE 2: WORKING DIRECTORY & ENVIRONMENT
# ==============================================================================
# Set working directory inside container
WORKDIR /app

# Set environment variables
# PYTHONUNBUFFERED=1: Print Python output immediately (better for logs)
# PYTHONDONTWRITEBYTECODE=1: Don't create .pyc files (cleaner container)
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FLASK_APP=app.py

# ==============================================================================
# STAGE 3: INSTALL DEPENDENCIES
# ==============================================================================
# If requirements.txt doesn't change, Docker reuses this layer (faster builds)
COPY requirements.txt .

# Install Python dependencies
# --no-cache-dir: Don't cache packages (smaller image size)
# --upgrade: Upgrade pip to latest version
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# ==============================================================================
# STAGE 4: COPY APPLICATION CODE
# ==============================================================================
# Copy all backend code into container
# (Excludes files listed in .dockerignore)
COPY . .

# ==============================================================================
# STAGE 5: CREATE NON-ROOT USER (SECURITY BEST PRACTICE)
# ==============================================================================
# Create a user called 'appuser' with no password
RUN adduser --disabled-password --gecos '' appuser && \
    chown -R appuser:appuser /app

# Switch to non-root user
USER appuser

# ==============================================================================
# STAGE 6: EXPOSE PORT
# ==============================================================================
EXPOSE 5000

# ==============================================================================
# STAGE 7: HEALTH CHECK
# ==============================================================================
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:5000/api/health')" || exit 1

# ==============================================================================
# STAGE 8: STARTUP COMMAND
# ==============================================================================
# Command to run when container starts
# Use Gunicorn in production (not Flask dev server)
# Gunicorn is production-ready WSGI HTTP Server
# --bind 0.0.0.0:5000: Listen on all network interfaces
# --workers 4: Use 4 worker processes (handles more requests)
# app:app: module:application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app:app"]
