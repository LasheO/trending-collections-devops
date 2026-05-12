# Frontend Dockerfile (Multi-Stage Build)
# 
# This file uses a multi-stage build approach:
# - Stage 1: Build the React app (large image with build tools)
# - Stage 2: Serve with nginx (small, production-ready image)
#
# Why multi-stage?
# - Final image is MUCH smaller (only contains built files, not build tools)
# - More secure (fewer packages = fewer vulnerabilities)
# - Faster deployment (smaller image to transfer)
#
# Author: Lashe Onamusi
# Date: December 2026
# Purpose: University DevOps Assignment - Containerization

# ==============================================================================
# STAGE 1: BUILD STAGE
# ==============================================================================
# Use Node.js to build the React application
FROM node:18-alpine AS builder

# Set metadata
LABEL stage=builder
LABEL description="Build stage for React frontend"

# Set working directory
WORKDIR /app

# Copy package files
# (Copy these first for Docker layer caching optimization)
COPY package*.json ./

# Install dependencies
# npm ci is faster and more reliable than npm install in CI/CD
RUN npm ci --only=production

# Copy all source code
COPY . .

# Build the React app for production
# Creates optimized static files in /app/build directory
RUN npm run build

# ==============================================================================
# STAGE 2: PRODUCTION STAGE
# ==============================================================================
# Use nginx to serve the built static files
# Nginx is a high-performance web server perfect for static content
FROM nginx:alpine

# Set metadata
LABEL maintainer="Lashe Onamusi"
LABEL description="Frontend for Trending Collections DevOps App"
LABEL version="1.0"

# Copy custom nginx configuration
# (We'll create this config file next)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Copy built React app from builder stage to nginx html directory
# --from=builder: Copy from the previous build stage
COPY --from=builder /app/build /usr/share/nginx/html

# Create non-root user for security
RUN addgroup -g 1001 -S appgroup && \
    adduser -u 1001 -S appuser -G appgroup && \
    chown -R appuser:appgroup /usr/share/nginx/html && \
    chown -R appuser:appgroup /var/cache/nginx && \
    chown -R appuser:appgroup /var/log/nginx && \
    chown -R appuser:appgroup /etc/nginx/conf.d && \
    touch /var/run/nginx.pid && \
    chown -R appuser:appgroup /var/run/nginx.pid

# Switch to non-root user
USER appuser

# Expose port 80 (HTTP)
EXPOSE 80

# Health check for nginx
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --quiet --tries=1 --spider http://localhost:80/ || exit 1

# Start nginx in foreground (default command)
# -g daemon off: Keep nginx in foreground (required for Docker)
CMD ["nginx", "-g", "daemon off;"]
