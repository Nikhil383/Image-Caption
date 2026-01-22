# Use python 3.11 slim as base
FROM python:3.11-slim-bookworm

# Install uv (The Python package manager)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# Set environment variables
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# Install dependencies using uv
COPY pyproject.toml uv.lock ./
# Copy source code for installation identification
COPY src/ src/
RUN uv sync --frozen --no-dev

# Copy the rest of the project (config, README, etc.)
COPY . .

# Create a non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose port 7860
EXPOSE 7860

# Run the application using gunicorn
CMD ["uv", "run", "gunicorn", "--bind", "0.0.0.0:7860", "image_caption.app:app"]
