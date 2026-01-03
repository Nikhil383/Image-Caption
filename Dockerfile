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
RUN uv sync --frozen --no-dev

# Copy the rest of the project
COPY . .

# Create a non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Expose port
EXPOSE 5000

# Run the application using uv run and gunicorn/flask
# For simplicity/dev, we use flask run. For prod, we'd use gunicorn.
# Using 'python -m flask' or just 'flask' via uv
CMD ["uv", "run", "python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
