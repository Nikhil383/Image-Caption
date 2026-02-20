from flask import Flask, render_template, request, flash, redirect, url_for
from PIL import Image, UnidentifiedImageError
from .models import generate_caption
import os
import io
import base64
import logging
from werkzeug.exceptions import RequestEntityTooLarge

# Configure logging
logging.basicConfig(
    level=logging.INFO if os.environ.get("FLASK_ENV") != "development" else logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

app = Flask(__name__)
# Use a secure secret key in production
app.secret_key = os.environ.get("SECRET_KEY", "super_secret_dev_key")

# Configure file upload size limit (default: 10MB)
max_size_mb = int(os.environ.get("MAX_CONTENT_LENGTH_MB", 10))
app.config['MAX_CONTENT_LENGTH'] = max_size_mb * 1024 * 1024

# Allowed image file extensions
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.gif', '.webp', '.bmp'}


def allowed_file(filename):
    """Check if file extension is allowed."""
    if not filename:
        return False
    ext = os.path.splitext(filename.lower())[1]
    return ext in ALLOWED_EXTENSIONS

@app.route("/", methods=["GET", "POST"])
def index():
    caption = None
    image_data = None
    
    if request.method == "POST":
        # Check if the post request has the file part
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
            
        file = request.files['image']
        
        # If user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
            
        if file:
            # Validate file extension
            if not allowed_file(file.filename):
                flash(f'Invalid file type. Allowed types: {", ".join(ALLOWED_EXTENSIONS)}')
                logger.warning(f"Rejected file upload: invalid extension - {file.filename}")
                return redirect(request.url)
            
            try:
                # Open image directly from stream (no save to disk needed)
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
                buffered = io.BytesIO()
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                image_data = f"data:image/jpeg;base64,{img_str}"
                
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

@app.errorhandler(RequestEntityTooLarge)
def handle_file_too_large(e):
    """Handle file size limit exceeded."""
    max_mb = app.config['MAX_CONTENT_LENGTH'] // (1024 * 1024)
    flash(f'File too large. Maximum size is {max_mb}MB.')
    logger.warning(f"File upload rejected: size limit exceeded")
    return redirect(request.url)


if __name__ == "__main__":
    # Host on 0.0.0.0 for Docker compatibility
    port = int(os.environ.get("PORT", 5000))
    debug = os.environ.get("FLASK_ENV") == "development"
    logger.info(f"Starting Flask app on port {port}, debug={debug}")
    app.run(debug=debug, host="0.0.0.0", port=port)
