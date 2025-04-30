# syntax=docker/dockerfile:1

##############################################################################
# 1. Builder stage: install uv and sync dependencies
##############################################################################
FROM python:3.12-slim-bookworm AS builder
LABEL maintainer="Your Name <you@example.com>"

# Install curl (needed for install script) and other build tools if required
RUN apt-get update \
 && apt-get install -y --no-install-recommends curl build-essential \
 && rm -rf /var/lib/apt/lists/*

# Install uv via pip (drop-in replacement for pip, pip-tools, venv, etc.)
RUN pip install --no-cache-dir uv \
    # verify installation
 && uv --version

WORKDIR /app

# Copy only dependency manifests
COPY ./pyproject.toml ./uv.lock  ./

# Use uv to install and lock dependencies into a virtual environment
RUN uv sync

##############################################################################
# 2. Final stage: copy over the uv binary, venv, and application code
##############################################################################
FROM python:3.12-slim-bookworm AS runtime

# Copy uv binary and the synced virtual environment from builder
COPY --from=builder /root/.local/bin/uv /usr/local/bin/uv
COPY --from=builder /app /app

WORKDIR /app

# Expose port if your application runs a web server
EXPOSE 8000

# Default to using uv to run your application
CMD ["uv", "run",  "start"]
