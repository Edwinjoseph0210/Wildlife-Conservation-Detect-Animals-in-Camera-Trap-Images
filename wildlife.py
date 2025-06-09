# Example: Using pre-trained YOLOv5 to detect animals in images
# Requires YOLOv5 repo and PyTorch

# Clone YOLOv5 repo:
# !git clone https://github.com/ultralytics/yolov5
# cd yolov5
# pip install -r requirements.txt

# Python code:
import torch
from matplotlib import pyplot as plt
import cv2

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# Load camera trap image
img = 'camera_trap.jpg'

# Inference
results = model(img)

# Results
results.print()
results.show()  # opens window
results.save()  # saves output image with bounding boxes
