# 🍎 Apple Detection App using YOLOv8

This is a simple Streamlit app that uses **YOLOv8** from the Ultralytics library to detect apples in uploaded images. It allows users to upload a `.jpg` or `.png` image and see the detection results with bounding boxes.

## 🚀 Features
- Upload any `.jpg` or `.png` image  
- Uses a pretrained **YOLOv8n** model for object detection  
- Visual confidence threshold slider for adjusting detection sensitivity  
- Displays both input and output (annotated) images  

## 🛠️ Tech Stack
- **Frontend/UI**: Streamlit  
- **Object Detection**: YOLOv8 (Ultralytics)  
- **Image Handling**: PIL, NumPy  
- **Language**: Python 3.8+  

## 📦 Setup Instructions

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```
2. **Run the App**

```bash
streamlit run app.py
```
