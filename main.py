from ultralytics import YOLO
import cv2


# load yolov8 model
model = YOLO("best_train4.pt")


# cap = cv2.imread("dining.png")

# result = model.track(image, persist=True)

# image = result[0].plot()

# cv2.imshow("Window name", image)
# cv2.waitKey(0)

# load video
cap = cv2.VideoCapture("tophighway.mp4")

ret = True
# read frames
while ret:
    ret, frame = cap.read()

    if ret:
        frame = frame[200:900, :]  # roi
        # detect objects
        # track objects
        results = model.track(frame, persist=True)

        # plot results
        # cv2.rectangle
        # cv2.putText
        frame_ = results[0].plot()

        # visualize
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)
        cv2.imshow("frame", frame_)
        if cv2.waitKey(0) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
