import streamlit as st
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image, UnidentifiedImageError
import os

# Set up the Streamlit app
st.title("Image Captioning with BLIP")
st.write("Upload an image to generate a caption.")

# Define the upload folder
UPLOAD_FOLDER = 'Images'

# Ensure the upload folder exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Load the BLIP model and processor once
@st.cache_resource
def load_model_and_processor():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    st.success("Model and processor loaded successfully!")
    return processor, model

# Load the model and processor
processor, model = load_model_and_processor()

def validate_image(image_path: str) -> bool:
    """Check if the file at image_path is a valid image."""
    if not os.path.exists(image_path):
        st.error(f"File not found: {image_path}")
        return False
    try:
        with Image.open(image_path) as img:
            return True
    except UnidentifiedImageError:
        st.error(f"Invalid image file: {image_path}")
        return False

def generate_caption(image: Image.Image, processor, model, max_length: int = 50) -> str:
    """Generate a caption for the provided image."""
    try:
        inputs = processor(images=image, return_tensors="pt")
        outputs = model.generate(**inputs, max_length=max_length)
        caption = processor.decode(outputs[0], skip_special_tokens=True)
        return caption
    except Exception as e:
        return f"An error occurred during caption generation: {str(e)}"

# Image upload
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Save the uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(filepath, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Validate and generate the caption
    if validate_image(filepath):
        image = Image.open(filepath)
        caption = generate_caption(image, processor, model)
        
        # Display the uploaded image and caption
        st.image(image, caption="Uploaded Image", use_column_width=True)
        st.subheader("Generated Caption:")
        st.write(caption)
    else:
        st.error("Invalid image file. Please upload a valid image.")