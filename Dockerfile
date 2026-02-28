# Use python 3.11 slim as base
FROM python:3.11-slim-bookworm

# Install system dependencies (important for torch, transformers etc.)
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Environment variables
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Copy only dependency files first (for Docker layer caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --no-dev

# Copy full project
COPY . .

# Create non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Render provides PORT dynamically
ENV PORT=10000

# Expose port (Render ignores EXPOSE but good practice)
EXPOSE 10000

# Start app
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:10000", "image_caption.app:app"]