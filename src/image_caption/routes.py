from flask import Blueprint, render_template, request, flash, redirect, current_app
from PIL import Image, UnidentifiedImageError
import logging

from .models import generate_caption, API_KEY
from .utils import allowed_file, image_to_base64
from .extensions import limiter

logger = logging.getLogger(__name__)
bp = Blueprint('main', __name__)

@bp.route("/", methods=["GET", "POST"])
@limiter.limit("10 per minute", methods=["POST"])
def index():
    caption = None
    image_data = None
    
    if request.method == "POST":
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
            
        file = request.files['image']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file:
            allowed_exts = current_app.config['ALLOWED_EXTENSIONS']
            if not allowed_file(file.filename, allowed_exts):
                flash(f'Invalid file type. Allowed types: {", ".join(allowed_exts)}')
                logger.warning(f"Rejected file upload: invalid extension - {file.filename}")
                return redirect(request.url)
            
            try:
                # Open image directly from stream
                image = Image.open(file.stream).convert('RGB')
                logger.info(f"Processing image: {file.filename}")

                # Generate caption
                caption = generate_caption(image)
                
                if caption.startswith("Error"):
                    flash("Failed to generate caption. Please try again with a different image.")
                    logger.error(f"Caption generation failed for {file.filename}")
                else:
                    logger.info(f"Caption generated successfully for {file.filename}")
                
                # Convert image to base64 for display
                image_data = image_to_base64(image)
                
            except UnidentifiedImageError:
                flash("Invalid image file. Please upload a valid image.")
                logger.warning(f"Unidentified image error for file: {file.filename}")
            except ValueError as e:
                flash("Invalid image format. Please try a different image.")
                logger.error(f"ValueError processing {file.filename}: {e}", exc_info=True)
            except Exception as e:
                flash("An error occurred while processing your image. Please try again.")
                logger.exception(f"Unexpected error processing {file.filename}: {e}")
                
    return render_template("index.html", caption=caption, image_data=image_data)

@bp.route("/health")
def health_check():
    """Liveness probe for Render."""
    status = "healthy" if API_KEY else "unconfigured"
    return {"status": status, "model": "gemini-1.5-flash"}, 200
