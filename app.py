# app.py
import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np

@st.cache_resource
def load_model():
    return YOLO(r'C:\Users\Admin\Internship\projects\Apple Detection\yolov8n.pt')

model = load_model()

st.title("Apple Detector with (YOLOv8)")
st.write("Please Upload an image.")

uploaded = st.file_uploader("Choose a .jpg or .png image", type=['jpg','jpeg','png'])

if uploaded:
    img = Image.open(uploaded).convert("RGB")
    st.image(img, caption="Input Image", use_column_width=True)

    
    thresh = st.slider("Confidence threshold value bar", 0.0, 1.0, 0.5, 0.05)

    
    results = model(img, conf=thresh)[0] # performing inference on the image

    annotated = results.plot()  # draw boxes on the image
    st.image(annotated, caption="Detected Apples", use_column_width=True)

   