import streamlit as st
from ultralytics import YOLO
from PIL import Image

# Load model once
model = YOLO("yolov8n.pt")

st.title("Nilima's YOLO Object Detector")

uploaded = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded is not None:
    # Show original image
    img = Image.open(uploaded)
    st.image(img, caption="Original image", use_container_width=True)

    # Run YOLO
    results = model(img)

    # Show result with boxes
    result_img = results[0].plot()
    st.image(result_img, caption="Detections", use_container_width=True)