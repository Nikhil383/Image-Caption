# Multimodal Image Captioning Engine

## Project Overview

This project implements an end-to-end Multimodal AI solution for automatically generating natural language descriptions (captions) from input images. It uses the **Salesforce/blip-image-captioning-base** model via the Hugging Face Transformers library.

## 🧠 Architectural Deep Dive

### BLIP Model
The application uses the **BLIP (Bootstrapping Language-Image Pre-training)** model.
-   **Vision Encoder (ViT)**: Processes the image into visual features.
-   **Text Decoder**: Generates the text caption based on the visual features.

## 🛠️ Technology Stack

| Category | Technology | Purpose |
| :--- | :--- | :--- |
| **Model** | BLIP Base | Image captioning model. |
| **Frameworks** | Streamlit | Web application interface. |
| **Libraries** | Transformers, Torch | Model loading and inference. |
| **Language** | Python 3.11+ | Primary programming language. |

## 🚀 Getting Started

### Prerequisites

Ensure you have Python installed. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the Application

Run the Streamlit app:

```bash
streamlit run main.py
```
Access at: `http://localhost:8501`

## 📂 Project Structure

```
.
├── main.py             # Main Streamlit application
├── models.py           # BLIP model integration
├── pyproject.toml      # Project dependencies
└── README.md           # Project documentation
```

## Author
[Your Name]

## License
MIT