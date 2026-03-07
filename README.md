# Multimodal Image Captioning Engine

## Problem Statement

Manual image captioning is slow, inconsistent, and does not scale. Many images lack descriptions, which hurts accessibility (e.g. for screen readers), SEO, and content management. This project addresses the need for an automated, scalable solution to overcome these bottlenecks and provide high-quality natural language captions for any image.

## Project Overview

This project implements an industrial-grade end-to-end Multimodal AI solution for automatically generating natural language descriptions (captions) from input images. It leverages the state-of-the-art **Google Gemini Vision** model, wrapped in a scalable **Flask** web application with a modern, responsive UI. It replaces legacy vision models with the blazing-fast and highly accurate Gemini API.

## Key Features

*   **Advanced AI Model**: Powered by **Google Gemini Flash** for blazing-fast, high-accuracy image understanding.
*   **Modern UI/UX**:
    *   Responsive design with polished CSS.
    *   **Drag & Drop** file upload support.
    *   **Instant Client-Side Preview**: Inspect your image immediately upon selection.
    *   **Visual Result**: Displays the uploaded image alongside the generated caption.
*   **Production Ready**:
    *   **Dockerized** for easy deployment.
    *   **Safe Dependency Management** using `uv`.

## Architecture

The application follows a standard client-server architecture integrating a cloud-based LLM:
-   **Client Layer**: A responsive web frontend (HTML/CSS/JS) capturing user image uploads via drag-and-drop or file selection.
-   **Server Layer**: A Flask backend that handles file validation, stream processing, and securely manages API communication.
-   **AI Layer**: integration with the **Google Gemini API** (`gemini-1.5-flash` / `gemini-2.5-flash`), transmitting image streams directly to the vision encoder for natural language caption generation.

## Technology stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Model** | Google Gemini Flash | SOTA Vision-to-Text API. |
| **Backend** | Flask | Lightweight, scalable web server. |
| **Frontend** | HTML5, CSS3, JS | Responsive interface with direct DOM manipulation. |
| **Libraries** | Google GenAI SDK | Interaction with Gemini API. |
| **DevOps** | UV, Docker | Fast dependency resolution & containerization. |
| **Language** | Python 3.11+ | Primary programming language. |

## Getting Started

### Prerequisites

*   **Google Gemini API Key**: Set your `GOOGLE_API_KEY` in your environment.
*   **uv**: A fast Python package installer and resolver.

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
docker run -p 5000:5000 -e GOOGLE_API_KEY=your_key_here image-caption
```

## Project Structure

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

## Learnings & challenges

**Learnings**:
*   **Modern Dependency Management**: Gained hands-on experience using `uv` over traditional package managers, discovering significant speed improvements in resolution and installation.
*   **Multimodal AI Integration**: Learned how to correctly format and stream image data (PIL) alongside text prompts to the Google Gemini API for seamless vision-language tasks.
*   **Robust Server-Side Handling**: Improved understanding of handling edge cases in Flask like file size limits (`RequestEntityTooLarge`) and stream processing without saving files to disk.

**Challenges**:
*   **Transitioning Architectures**: Adapting the initial architecture to utilize external APIs (Gemini) required refactoring the expected model loading and inference logic previously designed for local models.
*   **Secure API Key Management**: Ensuring the API Key was securely loaded in the environment and correctly handled both locally and in Docker without exposing it.
*   **UI/UX State Management**: Implementing a smooth client-side preview for the uploaded image and managing the loading states gracefully before the backend returned the generated caption.

## Demo

<img width="1919" height="928" alt="image" src="https://github.com/user-attachments/assets/85437049-0149-4379-a8d4-f98faf287928" />

<img width="1916" height="972" alt="image" src="https://github.com/user-attachments/assets/2f95d080-b609-492e-8f79-e7ba8f1ce297" />

- Deployment link for the app: [Link](https://image-caption-ejph.onrender.com)

## Author
Nikhil Mahesh

## License
MIT

