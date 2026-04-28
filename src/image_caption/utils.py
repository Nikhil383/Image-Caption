import os
import io
import base64
from PIL import Image

def allowed_file(filename: str, allowed_extensions: set) -> bool:
    """Check if file extension is allowed."""
    if not filename:
        return False
    ext = os.path.splitext(filename.lower())[1]
    return ext in allowed_extensions

def image_to_base64(image: Image.Image) -> str:
    """Convert a PIL Image to a base64 string for HTML display."""
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    return f"data:image/jpeg;base64,{img_str}"
