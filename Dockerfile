FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1

# System dependencies (needed for torch + transformers + pillow)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    curl \
    ca-certificates \
    libgl1 \
    ffmpeg \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install --no-cache-dir uv

# Copy only dependency files first (better caching)
COPY pyproject.toml uv.lock ./

# 🔥 REMOVE --frozen (causing failure on Render)
RUN uv sync --no-dev

# Copy rest of project
COPY . .

# Render dynamic port
ENV PORT=10000
EXPOSE 10000

# Use uv run
CMD ["sh", "-c", "uv run gunicorn --bind 0.0.0.0:$PORT src.app:app"]