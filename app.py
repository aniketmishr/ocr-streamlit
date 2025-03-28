import streamlit as st
import numpy as np
from PIL import Image
import easyocr

reader = easyocr.Reader(['en'],model_storage_directory='model') # this needs to run only once to load the model into memory

# Streamlit UI
st.set_page_config(page_title="OCR App", layout="wide")  # Set wide layout

st.sidebar.title("📄 ExtractAI:\nText Extraction App")
st.sidebar.write("Upload an image and extract text from it.")

# File uploader in sidebar
uploaded_file = st.sidebar.file_uploader("Choose an image...", type=["png", "jpg", "jpeg"])

# Main content layout
col1, col2 = st.columns([1, 1])  # Split screen into two equal columns

if uploaded_file is not None:
    # Load image
    image = Image.open(uploaded_file)

    # Display image on the left side
    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    # Extract text
    with st.spinner("Extracting text..."):
        extracted_text = "\n".join(reader.readtext(np.array(image), detail=0, paragraph = True))

    # Display extracted text on the right side
    with col2:
        st.subheader("Extracted Text:")
        st.text_area("", extracted_text, height=400)
else:
    st.write("⬅️ Upload an image from the sidebar to begin!")

