# app.py
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import cv2
import numpy as np
from skimage.feature import hog
from joblib import load

# Title
st.set_page_config(page_title="Hindi Digit Recognition", layout="centered")
st.title("🖋️ Draw Hindi Digit and Recognize")

# Model selection
model_choice = st.selectbox("Choose Model", ["SVM", "KNN"])
model_path = f"models/{model_choice.lower()}_model.joblib"
model = load(model_path)

# HOG parameters
hog_params = {
    "orientations": 9,
    "pixels_per_cell": (8, 8),
    "cells_per_block": (2, 2),
    "block_norm": 'L2-Hys'
}

st.markdown("### 🖌️ Draw inside the box below")
canvas_result = st_canvas(
    fill_color="white",
    stroke_width=10,
    stroke_color="black",
    background_color="white",
    height=280,
    width=280,
    drawing_mode="freedraw",
    key="canvas",
)

# Process the drawn image
if canvas_result.image_data is not None:
    img = canvas_result.image_data
    gray = cv2.cvtColor(img.astype("uint8"), cv2.COLOR_RGBA2GRAY)
    resized = cv2.resize(gray, (32, 32), interpolation=cv2.INTER_AREA)
    st.image(resized, caption="🧼 Processed Image (32x32)", width=150)

    # Extract HOG
    features = hog(resized, visualize=False, **hog_params).reshape(1, -1)

    if st.button("🔍 Predict"):
        prediction = model.predict(features)[0]
        st.success(f"🧠 Predicted Hindi Digit: {prediction}")
