import streamlit as st
from PIL import Image
from models import generate_caption

# Page Configuration
st.set_page_config(
    page_title="AI Image Captioner",
    page_icon="🖼️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# Custom CSS
st.markdown("""
<style>
    .main {
        background-color: #f8f9fa;
    }
    .stButton>button {
        width: 100%;
        background-color: #4CAF50;
        color: white;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .caption-box {
        background-color: white;
        color: #333333; /* Dark text color for visibility */
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
        border-left: 5px solid #4CAF50;
    }
    h1 {
        color: #2c3e50;
        font-family: 'Helvetica Neue', sans-serif;
    }
</style>
""", unsafe_allow_html=True)

st.title("AI Image Captioning Tool")
st.markdown("### Transform your images into descriptive text with BLIP.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_container_width=True)
    
    if st.button('Generate Caption'):
        with st.spinner('Analyzing visuals...'):
            try:
                caption = generate_caption(image)
                if "Error" in caption:
                    st.error(caption)
                else:
                    st.markdown(f"""
                        <div class="caption-box">
                            <h3>✨ AI Description:</h3>
                            <p>{caption}</p>
                        </div>
                    """, unsafe_allow_html=True)
            except Exception as e:
                st.error(f"An error occurred: {e}")

st.markdown("---")
st.markdown("Built using Streamlit and Transformers.")