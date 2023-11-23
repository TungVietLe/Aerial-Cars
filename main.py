from ultralytics import YOLO
import cv2
from distance import DistanceManager


# load yolov8 model
model = YOLO("best_train4.pt")
distanceMana = DistanceManager()

# load video
cap = cv2.VideoCapture("tophighway.mp4")
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"FPS: {fps}")


ret = True
# read frames
while ret:
    ret, frame = cap.read()
    frame = frame[200:900, :]  # roi

    if ret:
        # detect objects
        # track objects
        results = model.track(frame, persist=True, classes=[0])
        distanceMana.setFrame(frame)
        distanceMana.setResults(results)

        # plot results
        # cv2.rectangle
        # cv2.putText
        frame = results[0].plot()

        # visualize
        # frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        cv2.imshow("frame", frame)
        if cv2.waitKey(0) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
