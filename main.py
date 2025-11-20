import streamlit as st
from transformers import pipeline
from PIL import Image

st.title("🖼️ AI Image Captioning Tool")
st.write("Upload an image, and the AI will describe what it sees.")

# Cache the model so it doesn't reload every time (Speed boost)
@st.cache_resource
def load_model():
    return pipeline("image-to-text", model="Salesforce/blip-image-captioning-base")

captioner = load_model()

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Display the image
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    
    # Generate Button
    if st.button('Generate Caption'):
        with st.spinner('Analyzing visuals...'):
            # processing
            results = captioner(image)
            caption = results[0]['generated_text']
            st.success(f"**AI Description:** {caption}")