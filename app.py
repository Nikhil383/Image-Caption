from flask import Flask, render_template, request, flash, redirect, url_for
from PIL import Image
from models import generate_caption
import os
import io
import base64

app = Flask(__name__)
# Use a secure secret key in production
app.secret_key = os.environ.get("SECRET_KEY", "super_secret_dev_key")

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
            try:
                # Open image directly from stream (no save to disk needed)
                image = Image.open(file.stream).convert('RGB')

                # Generate caption
                caption = generate_caption(image)
                
                # Convert image to base64 for display
                buffered = io.BytesIO()
                image.save(buffered, format="JPEG")
                img_str = base64.b64encode(buffered.getvalue()).decode()
                image_data = f"data:image/jpeg;base64,{img_str}"
                
            except Exception as e:
                flash(f"Error processing image: {e}")
                
    return render_template("index.html", caption=caption, image_data=image_data)

if __name__ == "__main__":
    # Host on 0.0.0.0 for Docker compatibility
    app.run(debug=True, host="0.0.0.0", port=5000)
