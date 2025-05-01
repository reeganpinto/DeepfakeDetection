import streamlit as st
from theme_manager import apply_theme
apply_theme()



# Apply styles



st.title("📈 Model Performance & Info")

st.markdown("""
Here you can learn more about each model used in this Deepfake Detection app.
""")

# Define your models' info (update values as you add more)
model_details = {
    "Custom CNN": {
        "Description": "A convolutional neural network built from scratch for binary image classification.",
        "Input Size": "128x128 RGB",
        "Accuracy": "91.4%",
        "Pros": "Fast, lightweight, trained for this dataset.",
        "Cons": "Might overfit or lack generalization."
    },
    "Transfer Learning (e.g. MobileNet, ResNet)": {
        "Description": "A model based on pre-trained ImageNet weights, fine-tuned for deepfake classification.",
        "Input Size": "224x224 RGB (typically)",
        "Accuracy": "93.8%",
        "Pros": "Strong feature extraction, generalizable.",
        "Cons": "Larger, slower inference."
    },
    "U-Net (if added later)": {
        "Description": "A U-shaped model typically used for segmentation but adapted here for classification.",
        "Input Size": "128x128 RGB",
        "Accuracy": "89.6%",
        "Pros": "Useful for localized features.",
        "Cons": "Not originally designed for classification tasks."
    }
}

for name, info in model_details.items():
    with st.expander(f"🧠 {name}"):
        st.write(f"**Description:** {info['Description']}")
        st.write(f"**Input Size:** {info['Input Size']}")
        st.write(f"**Accuracy:** {info['Accuracy']}")
        st.write(f"**Pros:** {info['Pros']}")
        st.write(f"**Cons:** {info['Cons']}")
