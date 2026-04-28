#  Multimodal Image Captioning Engine

**An end-to-end AI SaaS platform for automated image description generation, deployed to production.**  
*Built with Google Gemini, Flask, Docker, and modern DevOps practices.*

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Render-brightgreen)](https://image-caption-ejph.onrender.com)

> **Live Application:** [https://image-caption-ejph.onrender.com](https://image-caption-ejph.onrender.com)

---

## Why This Project Matters

In an era where **digital content accessibility** is both a legal requirement and ethical imperative, this platform solves a real-world problem:

| **Before** | **After** |
|:-----------|:----------|
| Manual image captioning (hours per batch) | Automated AI captioning (seconds per image) |
| Inconsistent quality across content teams | Standardized, high-quality descriptions |
| Accessibility compliance gaps | WCAG-compliant alt-text generation |
| SEO-impoverished image assets | Enhanced search discoverability |

---

##  Project Highlights

###  Core Capabilities
- **Multimodal Vision-Language AI**: Integrates Google Gemini Flash (SOTA vision model) for high-accuracy image understanding
- **Real-time Processing**: Stream-based API handling with instant client-side feedback
- **Production Pipeline**: Containerized microservice architecture with automated dependency management
- **Modern UX**: Drag-and-drop uploads, instant previews, responsive design

###  Technical Complexity

```python
# Architected for scale and maintainability
┌─────────────┐     ┌─────────────┐     ┌─────────────────┐
│  React-like │────▶│   Flask     │────▶│ Google Gemini   │
│    HTML/JS  │◀────│   FastAPI   │◀────│   Vision API    │
└─────────────┘     └─────────────┘     └─────────────────┘
    Frontend          Backend Layer          AI Layer
   (Vanilla ES6)    (Python 3.11+)        (Cloud ML)
```

**Engineering Decisions Demonstrated:**
-  **Security-first**: API key management via environment variables, no secrets in code
-  **Performance**: Stream processing without disk I/O, efficient image-to-API serialization
-  **Reliability**: Comprehensive error handling, request size limits, graceful degradation
-  **DevOps**: Docker multi-stage builds, `uv` for sub-second dependency resolution

---

##  Technology Stack

| Layer | Technology | How I Used It |
|:-----:|:-----------|:--------------|
| **AI/ML** | Google Gemini Flash | Multimodal vision-to-text inference via streaming API |
| **Backend** | Python 3.11 + Flask | RESTful API design, request validation, error handling |
| **Frontend** | Vanilla JS + CSS3 | Dynamic DOM manipulation, async fetch API, responsive grid |
| **DevOps** | Docker + UV | Multi-stage containerization, lockfile-based reproducibility |
| **Deployment** | Render | Production-grade PaaS deployment with auto-scaling |

---

##  Architecture Overview

```
User Upload (Drag & Drop)
    ↓
Client-Side Preview (JS FileReader API)
    ↓
Flask Endpoint (/predict)
    ↓
Image Preprocessing (PIL → BytesIO stream)
    ↓
Google GenAI SDK → Gemini Vision API
    ↓
Streaming Response → JSON Payload
    ↓
Dynamic DOM Update (Caption + Image Display)
```

**Key Technical Challenge Solved:**  
*Transitioned from local PyTorch models to cloud-based API architecture, implementing efficient stream-to-API serialization while maintaining sub-3-second response times.*

---

##  Quick Start

```bash
# Clone & setup
git clone <repo>
cd image-caption
uv sync

# Run locally
make run
# → http://localhost:5000

# Or with Docker
docker build -t image-caption . && docker run -p 5000:5000 -e GOOGLE_API_KEY=$GOOGLE_API_KEY image-caption
```

---

##  Project Structure

```
image-caption/
├── src/image_caption/
│   ├── app.py           # Flask application entry point
│   ├── models.py        # Gemini API integration & stream handling
│   ├── templates/       # Jinja2 templates (HTML)
│   └── static/          # CSS, JS, assets
├── tests/               # pytest suite
├── pyproject.toml       # PEP 621 project config
├── uv.lock             # Reproducible dependency lock
├── Dockerfile          # Production container
└── Makefile            # Development shortcuts
```

---

##  What I Learned

| Challenge | Solution | Skill Demonstrated |
|:----------|:---------|:-------------------|
| API key security across local/dev/prod | Environment variable abstraction with Docker secrets | Secure deployment practices |
| High-latency cloud API calls | Stream processing + async loading states | UX optimization for async workflows |
| Dependency hell | Migrated to `uv` with lockfile enforcement | Modern Python tooling |
| Cross-platform deployment | Multi-stage Docker builds, Render pipeline | CI/CD fundamentals |

---

##  Demo

### Upload Interface
![Upload View](https://github.com/user-attachments/assets/85437049-0149-4379-8a4d-f98faf287928)

### Caption Generated
![Result View](https://github.com/user-attachments/assets/2f95d080-b609-492e-8f79-e7ba8f1ce297)

**Try it yourself:** [https://image-caption-ejph.onrender.com](https://image-caption-ejph.onrender.com)

---

##  License

MIT © Nikhil Mahesh

---

*This project was built to demonstrate production-grade AI application development—from model integration to deployment.*
