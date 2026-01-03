# Multimodal Image Captioning Engine

## Project Overview

This project implements an industrial-grade end-to-end Multimodal AI solution for automatically generating natural language descriptions (captions) from input images. It leverages the **Salesforce/blip-image-captioning-base** model via Hugging Face Transformers, wrapped in a scalable **Flask** web application with a modern, responsive UI.

## Key Features

*   **Advanced AI Model**: Uses BLIP (Bootstrapping Language-Image Pre-training) for high-accuracy image understanding.
*   **Modern UI/UX**:
    *   Responsive design with polished CSS.
    *   **Drag & Drop** file upload support.
    *   **Instant Client-Side Preview**: Inspect your image immediately upon selection.
    *   **Visual Result**: Displays the uploaded image alongside the generated caption.
*   **Production Ready**:
    *   **Dockerized** for easy deployment.
    *   **Safe Dependency Management** using `uv`.
    *   **Thread-Safe** model loading (Singleton pattern).

## Architecture

### BLIP Model
The application uses the **BLIP (Bootstrapping Language-Image Pre-training)** model.
-   **Vision Encoder (ViT)**: Processes the image into visual features.
-   **Text Decoder**: Generates the text caption based on the visual features.

## Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Model** | BLIP Base | Image captioning model. |
| **Backend** | Flask | Lightweight, scalable web server. |
| **Frontend** | HTML5, CSS3, JS | Responsive interface with direct DOM manipulation. |
| **ML Libraries** | Transformers, Torch | Model loading and inference. |
| **DevOps** | UV, Docker | Fast dependency resolution & containerization. |
| **Language** | Python 3.11+ | Primary programming language. |

## Getting Started

### Prerequisites

Ensure you have **uv** installed (a fast Python package installer and resolver).

```bash
pip install uv
```

### Installation

Sync dependencies using `uv`:

```bash
uv sync
```

### Running the Application

Run the Flask app server:

```bash
uv run python -m flask run
```
Access the application at: `http://localhost:5000`

### Running with Docker

Build and run the containerized application:

```bash
docker build -t image-caption .
docker run -p 5000:5000 image-caption
```

##  Project Structure

```
.
├── app.py              # Flask entry point & route logic
├── models.py           # Thread-safe ML model integration
├── templates/          # HTML templates with JS logic
├── static/             # Modern CSS styling
├── Dockerfile          # Multi-stage Docker build
├── pyproject.toml      # Project configuration & dependencies
└── uv.lock             # Exact dependency lockfile
```

## Author
Nikhil Mahesh

## License
MIT