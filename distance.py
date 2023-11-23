import cv2


class DistanceManager:
    def __init__(self) -> None:
        self.frame = None
        self.ids = {}

    def setFrame(self, frame):
        self.frame = frame

    def setResults(self, results):
        # for result in results.boxes.xywh:
        #     c = result.boxes.xywh.tolist()[0]  # To get the coordinates.
        #     x, y, w, h = c[0], c[1], c[2], c[3]  # x, y are the center coordinates.
        #     print((x, y))
        #     cv2.circle(
        #         self.frame, (int(x), int(y)), radius=3, color=(255, 0, 0), thickness=-1
        #     )

        for result in results:
            print("RESULT IN RESULTS")
            id = 0
            for tensorID in result.boxes.id:
                box = result.boxes.xywh[id]
                x, y, w, h = (
                    box[0],
                    box[1],
                    box[2],
                    box[3],
                )  # x, y are the center coordinates.
                cv2.circle(
                    self.frame,
                    (int(x), int(y)),
                    radius=3,
                    color=(255, 0, 0),
                    thickness=-1,
                )
                id += 1

                # Compare distance to previous frame
                if self.ids.get(int(tensorID)) is not None:
                    prevCenter = self.ids.get(int(tensorID))
                    cv2.line(self.frame, (int(x), int(y)), prevCenter, (255, 255, 0), 3)

                    # calculate speed
                    M_S2KM_H = 3.6
                    speed = round(
                        (int(x) - prevCenter[0]) * 0.021 * 24 * M_S2KM_H, ndigits=1
                    )
                    cv2.putText(
                        self.frame,
                        f"velX: {speed} km/h",
                        (int(x), int(y)),
                        cv2.FONT_HERSHEY_PLAIN,
                        2,
                        (255, 255, 255),
                        3,
                    )

                # Replace previous frame with this frame
                self.ids[int(tensorID)] = (int(x), int(y))
                print(self.ids)
