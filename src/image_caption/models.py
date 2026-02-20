from transformers import pipeline
from PIL import Image
import threading
import logging

logger = logging.getLogger(__name__)

# Singleton pattern for the model to ensure it's removed from global scope if we move to a class-based system,
# but for now we use a lazy loading approach.

class CaptionModel:
    _instance = None
    _lock = threading.Lock()
    _model_name = "Salesforce/blip-image-captioning-base"

    @classmethod
    def get_pipeline(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    logger.info(f"Loading model: {cls._model_name}...")
                    cls._instance = pipeline("image-to-text", model=cls._model_name)
                    logger.info("Model loaded successfully.")
        return cls._instance

def generate_caption(image: Image.Image) -> str:
    """
    Generates a caption for the given image using the BLIP model.
    
    Args:
        image (PIL.Image.Image): The input image to caption.
        
    Returns:
        str: The generated caption or an error message.
    """
    try:
        # Get the model instance (lazy loaded)
        captioneer = CaptionModel.get_pipeline()
        
        # Inference
        results = captioneer(image)
        
        # Validation
        if not results or "generated_text" not in results[0]:
            raise ValueError("Model returned unexpected format.")
            
        return results[0]["generated_text"]
        
    except ValueError as e:
        logger.error(f"Model validation error: {e}")
        return "Error analyzing image: Invalid model response."
    except Exception as e:
        logger.exception(f"Unexpected error during caption generation: {e}")
        return "Error analyzing image: An unexpected error occurred."

if __name__ == "__main__":
    # Test load
    CaptionModel.get_pipeline()