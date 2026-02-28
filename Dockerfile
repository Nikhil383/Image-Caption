FROM python:3.11-slim

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV UV_LINK_MODE=copy
ENV UV_COMPILE_BYTECODE=1

# System dependencies
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

# Copy dependency files + README (IMPORTANT FIX)
COPY pyproject.toml uv.lock README.md ./

# Install dependencies
RUN uv sync --no-dev

# Copy rest of project
COPY . .

ENV PORT=10000
EXPOSE 10000

CMD ["sh", "-c", "uv run gunicorn --bind 0.0.0.0:$PORT src.app:app"]