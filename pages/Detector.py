import streamlit as st
from theme_manager import apply_theme
apply_theme()

# Continue your app logic
import tensorflow as tf
from tensorflow.keras.models import load_model

from PIL import Image
import numpy as np
import time

@st.cache_resource
def load_models():
    models = {
        "Custom CNN": load_model("models_utils/deepfake_custom_model.h5"),
        "U-Net": load_model("models_utils/deepfake_unet_model.h5"),
        "Updated-Unet": load_model("models_utils/deepfake_updated_unet_model.h5")
    }
    return models

models = load_models()

st.title("🔍 Deepfake Image Detector")
st.markdown("Upload an image to detect if it's **Real or Fake** using a selected model.")

model_choice = st.selectbox("Choose a model:", list(models.keys()))
model = models[model_choice]

uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((128, 128))
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    if st.button("🔍 Predict"):
        with st.spinner("Analyzing image..."):
            start = time.time()

            input_data = preprocess_image(image)
            prediction = model.predict(input_data)[0][0]
            label = "Fake" if prediction >= 0.5 else "Real"
            confidence = prediction if label == "Fake" else 1 - prediction

            elapsed = time.time() - start
            if elapsed < 2:
                time.sleep(2 - elapsed)

        col1, col2 = st.columns(2)
        with col1:
            color = "red" if label == "Fake" else "green"
            emoji = "😡" if label == "Fake" else "😊"
            st.markdown(f"<h3 style='color:{color};'>{label} {emoji}</h3>", unsafe_allow_html=True)

        with col2:
            st.metric(label="Confidence", value=f"{confidence:.2%}")
