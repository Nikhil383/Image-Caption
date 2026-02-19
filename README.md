# Multimodal Image Captioning Engine

## Problem Statement

Manual image captioning is slow, inconsistent, and does not scale. Many images lack descriptions, which hurts accessibility (e.g. for screen readers), SEO, and content management. This project addresses that by providing an end-to-end, production-ready system that generates accurate, natural-language captions from images using a state-of-the-art vision–language model (BLIP), with a simple web interface and Docker deployment.

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

Using Make:

```bash
make run
```

Or manually:

```bash
uv run python -m image_caption.app
```
Access the application at: `http://localhost:5000`

### Running with Docker

Build and run the containerized application:

```bash
make docker-build
make docker-run
```

##  Project Structure

```
.
├── src/
│   └── image_caption/  # Main package
│       ├── app.py      # Flask entry point
│       ├── models.py   # Model integration
│       ├── templates/  # Javascript/HTML
│       └── static/     # CSS/Images
├── tests/              # Test suite (pytest)
├── notebooks/          # Jupyter notebooks
├── Makefile            # Command shortcuts
├── Dockerfile          # Production Dockerfile
├── pyproject.toml      # Project configuration
└── uv.lock             # Dependency lockfile
```

## Author
Nikhil Mahesh

## License
MIT