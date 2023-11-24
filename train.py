from ultralytics import YOLO

# Load a model

model = YOLO(model="best_train9.pt").load("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="data.yaml", epochs=6, patience=3, device='mps')  # train the model
# metrics = model.val()  # evaluate model performance on the validation set
# results = model("https://ultralytics.com/images/bus.jpg")  # predict on an image
path = model.export()  # export the model to ONNX format
