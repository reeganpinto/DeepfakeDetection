import streamlit as st
from theme_manager import apply_theme

st.set_page_config(page_title="Deepfake Detection App", layout="centered")

apply_theme()





# Apply custom styles


# Page content
st.title("🧠 Welcome to the Deepfake Detection App")

st.markdown("""
This app helps detect whether an image is **Real or Fake** using pre-trained deep learning models.

Use the sidebar to navigate between pages:

- **🔍 Deepfake Detector**: Upload an image and test it.
- **📊 Model Stats** : Checkout the accuracies for different models
""")


