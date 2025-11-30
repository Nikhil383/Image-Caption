from transformers import pipeline
from PIL import Image

# Initialize the pipeline once to avoid reloading it
# Use a pipeline as a high-level helper
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

def generate_caption(image: Image.Image):
    """Generates a caption for the given image using Salesforce/blip-image-captioning-base."""
    try:
        results = captioner(image)
        # The result is a list of dictionaries, e.g., [{'generated_text': 'a caption'}]
        return results[0]['generated_text']
    except Exception as e:
        return f"Error generating caption: {e}"

if __name__ == "__main__":
    print("Model loaded successfully.")