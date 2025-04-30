import streamlit as st
from tensorflow.keras.models import load_model # type: ignore
from PIL import Image
import numpy as np

# Load the model once
@st.cache_resource
def load_model_once():
    return load_model("deepfake_custom_model.h5")

model = load_model_once()

# UI
st.title("Deepfake Image Detector 🔍")
st.write("Upload an image to detect whether it's Real or Fake using the Custom CNN model.")

# Upload image
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

# Preprocess function
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((128, 128))  # Must match model input size
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Prediction logic
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    if st.button("Predict"):
        input_data = preprocess_image(image)
        prediction = model.predict(input_data)[0][0]
        label = "Fake" if prediction >= 0.5 else "Real"
        confidence = prediction if label == "Fake" else 1 - prediction

        st.markdown(f"### Result: **{label}**")
        st.markdown(f"Confidence: `{confidence:.2%}`")
