import google.generativeai as genai
from PIL import Image
import os
import logging
from typing import Optional
from dotenv import load_dotenv

# Load environment variables for local development
load_dotenv()

logger = logging.getLogger(__name__)

# Configure the Gemini API
API_KEY = os.environ.get("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    logger.error("GOOGLE_API_KEY not found in environment variables.")

def generate_caption(image: Image.Image) -> str:
    """
    Generates a caption for the given image using the Google Gemini model.
    
    Args:
        image (PIL.Image.Image): The input image to caption.
        
    Returns:
        str: The generated caption or an error message.
    """
    try:
        if not API_KEY:
            return "Error: GOOGLE_API_KEY is not configured. Please set it in your environment."

        # Use the gemini-1.5-flash model which is fast and efficient for vision tasks
        model = genai.GenerativeModel("gemini-2.5-flash")
        
        # Construct the prompt
        prompt = "Write a concise, descriptive caption for this image."
        
        # Generate the content
        # Note: we pass the image directly (PIL.Image is supported by the SDK)
        response = model.generate_content([prompt, image])
        
        # Validation
        if not response or not response.text:
            raise ValueError("Gemini API returned an empty response.")
            
        return response.text.strip()
        
    except ValueError as e:
        logger.error(f"API validation error: {e}")
        return "Error analyzing image: The AI returned an invalid response."
    except Exception as e:
        logger.exception(f"Unexpected error during caption generation: {e}")
        return f"Error analyzing image: {str(e)}"

if __name__ == "__main__":
    # Test block
    if not API_KEY:
        print("Set GOOGLE_API_KEY env var to run this test.")
    else:
        # Create a tiny dummy image for testing
        dummy_img = Image.new('RGB', (10, 10), color='red')
        caption = generate_caption(dummy_img)
        print(f"Test Caption: {caption}")