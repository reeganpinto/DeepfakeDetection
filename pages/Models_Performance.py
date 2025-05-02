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
        "Accuracy": "68.5%",
        "Pros": "Fast, lightweight, trained for this dataset.",
        "Cons": "Might overfit or lack generalization."
    },
    
    
    "U-Net": {
        "Description": "A U-shaped model typically used for segmentation but adapted here for classification.",
        "Input Size": "128x128 RGB",
        "Accuracy": "72.2%",
        "Pros": "Useful for localized features.",
        "Cons": "Not originally designed for classification tasks."
    },
    "DenseNet": {
       "Description": "A densely connected CNN architecture where each layer receives inputs from all preceding layers, promoting feature reuse.",
       "Input Size": "224x224 RGB",
       "Accuracy": "84.65%",  # Adjust based on your model
       "Pros": "Excellent feature propagation and efficient parameter usage; good performance on complex datasets.",
       "Cons": "Higher memory consumption; slower training compared to simpler models."
    },

    "EfficientNet": {
       "Description": "A highly efficient and scalable CNN model that balances depth, width, and resolution using a compound scaling method.",
       "Input Size": "224x224 RGB",
       "Accuracy": "83.22%",  # Adjust based on your training results
       "Pros": "State-of-the-art accuracy with fewer parameters; good generalization.",
       "Cons": "Slightly slower inference on low-end hardware; larger model size compared to custom CNN."
    },
    "ResNet50": {
       "Description": "A deep residual network that uses skip connections to prevent vanishing gradients and allow training of very deep architectures.",
       "Input Size": "224x224 RGB",
       "Accuracy": "81%",  # Modify based on your training/testing results
       "Pros": "Strong performance on various vision tasks; robust against overfitting with deep layers.",
       "Cons": "Larger model; slightly slower inference and training times compared to lightweight models."
}



}

for name, info in model_details.items():
    with st.expander(f"🧠 {name}"):
        st.write(f"**Description:** {info['Description']}")
        st.write(f"**Input Size:** {info['Input Size']}")
        st.write(f"**Accuracy:** {info['Accuracy']}")
        st.write(f"**Pros:** {info['Pros']}")
        st.write(f"**Cons:** {info['Cons']}")
