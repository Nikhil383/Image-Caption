# Industrial-Level Improvement Plan for Image Captioning Project

This document outlines a roadmap to elevate the current Image Captioning AI project to an industrial-grade standard.

## 1. Dependency Management & Virtual Environment

*   **Current State**: `pyproject.toml` contains unused dependencies (`flask`, `google-generativeai`, `python-dotenv`).
*   **Recommendation**:
    *   **Cleanup**: Remove unused libraries to reduce the Docker image size and security surface area.
    *   **Locking**: Continue using `uv.lock` (which you already have) to ensure deterministic builds.
    *   **Separation**: Separate `dev-dependencies` (e.g., `pytest`, `black`, `ruff`) from production dependencies.

## 2. Architecture & Code Structure

*   **Current State**: Monolithic script logic with basic separation (`main.py` -> `models.py`). `models.py` loads the model at module level.
*   **Recommendation**:
    *   **Caching**: In `models.py`, wrap the model loading in a function decorated with `@st.cache_resource` (if keeping Streamlit) or implement a Singleton pattern if moving to an API. This prevents reloading the heavy model on every script rerun (common in Streamlit).
    *   **Configuration**: Move hardcoded strings (model name `"Salesforce/blip-image-captioning-base"`) to a config class or environment variables (using `pydantic-settings`).
    *   **Typing**: Add type hints (already partially present) and use a type checker like `mypy` in strict mode.

## 3. Backend & API (Scalability)

*   **Current State**: Streamlit acts as both frontend and backend. This is not scalable for high concurrency.
*   **Recommendation**:
    *   **Decoupling**: Create a robust backend implementation using **FastAPI**.
        *   Endpoint: `POST /predict` that accepts an image and returns JSON.
        *   Async: Use `async` handlers to handle concurrent requests better (though model inference itself is CPU/GPU bound and might need run_in_executor).
    *   **Frontend**: Keep Streamlit for the internal demo, but consumes the FastAPI endpoint instead of importing `models.py` directly. Or build a React/Next.js frontend for a true consumer product.

## 4. Containerization & Deployment

*   **Current State**: No `Dockerfile`.
*   **Recommendation**:
    *   **Docker**: Create a multi-stage `Dockerfile`.
        *   *Builder Stage*: Install dependencies.
        *   *Runtime Stage*: Copy venv and code, keeping the image light.
    *   **Docker Compose**: If adding a separate backend (FastAPI) and frontend (Streamlit/React), use `docker-compose.yml` to orchestrate them.

## 5. Testing & Quality Assurance

*   **Current State**: No tests.
*   **Recommendation**:
    *   **Unit Tests**: Add `pytest`. Test the `generate_caption` function with a mock model or a small dummy image.
    *   **Integration Tests**: Test the full flow from image load to caption output.
    *   **Linting**: Add `ruff` or `flake8` for linting and `black` for formatting. Set up `pre-commit` hooks.

## 6. Observability & Logging

*   **Current State**: Using `print` and `st.error`.
*   **Recommendation**:
    *   **Logging**: Use Python's `logging` module or `loguru`. Log important events (model loaded, request received, error occurred) with timestamps.
    *   **Monitoring**: In a real "industrial" setting, you'd add Prometheus metrics (latency, request count) or use a tool like Sentry for error tracking.

## 7. Model Optimization

*   **Current State**: Loading standard float32 (likely) model on CPU.
*   **Recommendation**:
    *   **Quantization**: Use 8-bit or 4-bit quantization (via `bitsandbytes` or `optimum`) to reduce memory usage and improved latency on CPUs.
    *   **ONNX**: Convert the model to ONNX format for faster inference using `ONNX Runtime`.

## Proposed Folder Structure
```
.
├── .github/workflows   # CI/CD
├── src/
│   ├── app/            # Streamlit/Frontend code
│   │   └── main.py
│   ├── api/            # FastAPI code
│   │   └── main.py
│   ├── core/           # Model logic
│   │   ├── config.py
│   │   └── model.py
│   └── utils/
├── tests/              # Pytest
├── .dockerignore
├── Dockerfile
├── pyproject.toml
└── README.md
```
