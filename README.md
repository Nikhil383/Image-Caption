# Multimodal Image Captioning Engine

## Problem Statement

Manual image captioning is slow, inconsistent, and does not scale. Many images lack descriptions, which hurts accessibility (e.g. for screen readers), SEO, and content management. This project addresses that by providing an end-to-end, production-ready system that generates accurate, natural-language captions from images using a state-of-the-art vision–language model (BLIP), with a simple web interface and Docker deployment.

## Project Overview

This project implements an industrial-grade end-to-end Multimodal AI solution for automatically generating natural language descriptions (captions) from input images. It leverages the **Salesforce/blip-image-captioning-base** model via Hugging Face Transformers, wrapped in a scalable **Flask** web application with a modern, responsive UI.

## Key Features

*   **Advanced AI Model**: Powered by **Google Gemini 1.5 Flash** for blazing-fast, high-accuracy image understanding.
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
| **Model** | Google Gemini 1.5 Flash | SOTA Vision-to-Text API. |
| **Backend** | Flask | Lightweight, scalable web server. |
| **Frontend** | HTML5, CSS3, JS | Responsive interface with direct DOM manipulation. |
| **Libraries** | Google GenAI SDK | Interaction with Gemini API. |
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
docker build -t image-caption .
docker run -p 5000:10000 -e GOOGLE_API_KEY=your_key_here image-caption
```

## Deployment on Render

1.  **Create a New Web Service**: Connect your GitHub repository.
2.  **Environment Variables**:
    *   `GOOGLE_API_KEY`: Your Gemini API key from [Google AI Studio](https://aistudio.google.com/).
    *   `SECRET_KEY`: A random string for Flask sessions.
3.  **Health Check**: Set the health check path to `/health`.
4.  **Runtime**: Docker (Render will use your `Dockerfile` automatically).

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
## Demo

<img width="1919" height="928" alt="image" src="https://github.com/user-attachments/assets/85437049-0149-4379-a8d4-f98faf287928" />

<img width="1916" height="972" alt="image" src="https://github.com/user-attachments/assets/2f95d080-b609-492e-8f79-e7ba8f1ce297" />


## Author
Nikhil Mahesh

## License
MIT
