# Yolo-mini-project-bynilima
YOLOv8 mini project - image + webcam detection

# YOLOv8 Real-Time Object Detection – Mini Project
This repository contains my mini project. It focuses on real-time object detection with YOLOv8 using Python, VS Code / Jupyter, and a simple Streamlit app.

## Project overview
- Implemented YOLOv8 object detection in Python using the ultralytics library.
- Ran inference on local images (e.g., test_img.jpg) and on a webcam stream.
- Saved annotated output images such as yolo_result_ram.jpg for documentation.
- Wrote clear, commented notebook cells so each step (setup, image detection, webcam, saving results) is easy to follow.

## Files in this repo
- nilima_yolo_project.ipynb – main Jupyter notebook with all steps (install, image detection, webcam, saving results).
- app.py – Streamlit app for uploading an image and viewing YOLOv8 detections.
- dog_img.jpg – example input image.
- yolo_result_nilima.jpg – example output image with bounding boxes and labels.

## How to run the notebook

1. Create a Python 3.12 environment.
2. Install dependencies:
  -> pip install ultralytics opencv-python pillow streamlit
3. Open yolo_project.ipynb in VS Code or Jupyter and run the cells in order.

How to run the Streamlit app
1. Make sure you installed the dependencies above.
2. From the project folder, run:
  -> streamlit run app.py
3. A browser window will open. Upload an image and the app will display YOLOv8 detections.
  Technologies used
   - Python, Jupyter / VS Code
   - YOLOv8 (ultralytics)
   - OpenCV
   - Streamlit
