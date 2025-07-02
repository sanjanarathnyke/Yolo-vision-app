from ultralytics import YOLO

model = YOLO("yolo11s.pt")  # Load a custom YOLOv11 model

result = model(source="0", show=True, conf=0.4, save=False)  # Use 0 for webcam input