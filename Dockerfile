FROM python:3.11-slim

WORKDIR /app

# Optimization: Don't write pyc, don't buffer stdout
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1
ENV PYTHONPATH=/app/src

# System dependencies (minimal for flask/pillow)
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install uv for fast dependency management
RUN pip install --no-cache-dir uv

# Copy project files
COPY pyproject.toml uv.lock README.md ./
COPY src/ src/

# Install dependencies excluding dev group
RUN uv sync --no-dev

# Render uses the PORT env var
ENV PORT=10000
EXPOSE 10000

# Start with gunicorn
# Note: Since the model is in the cloud (Gemini), we can use more workers!
CMD ["sh", "-c", "uv run gunicorn --bind 0.0.0.0:$PORT --workers 4 --access-logfile - --error-logfile - image_caption.app:app"]