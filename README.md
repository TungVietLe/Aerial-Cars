# Aerial-Cars

Object dection and speed estimation.

![export with id](/assets/gif/export_video_withID.gif)

## Training

- As I have a relatively low-end computer, I only used `yolov8n`, which means there is wide room for improvement if I use a more powerful one, such as `yolov8l` or `yolov8x`.
- 28 epoch - 1.3 hours
- 367 images - 416x416
- dataset details can be found [here](https://github.com/TungVietLe/Aerial-Cars/blob/main/README.roboflow.txt)

- What I observed in the last few epochs is that the mAP50 and mAP50-95 barely improve. I ran a few more epoch after with (patience=4) and it stops prematurely, which means the model stops improving. However, at the same time, the `patience` value is really low to draw any meaningful conclusion.

![result](./assets/imgs/train4_result.png)
_latest training result (yolov8n)._

_the model trained mostly on "far view" dataset, such that I tried to use it on this video_

## Calculations

- **The idea is fairly simple:** since the camera is positioned top-down, if we know the pixel distance a car move in the frame, we can translate it into real-world measurements.
- I use the following source:

![road_graph](./assets/imgs/1_road.png)

![highlight_data](./assets/imgs/2_highlight.png)

![to_real_measure](./assets/imgs/3_to_real.jpg)

- Based on these, we can see that: `speedX = distanceX * meter_per_pixel * fps` (each frame)

- To get the distance, simply store the `id` of each car in a dictionary, then compare and update it every frame (or any duration of time).

![export](/assets/gif/export_video.gif)

## Initial approach (motion detection)

My initial approach is to use Motion detection + Custom tracking based on distance, but later I decided to use `yolov8` for expansion potential and learning purposes.

![tracking_tracking_in_roi](./assets/imgs/tracking_tracking_in_roi.png)

_initial idea of tracking + assigning id in ROI (region of interest)_

![roi](./assets/imgs/roi_and_detection.png)

![roi](./assets/gif/export_video_motion_detect.gif)

_results of the initial 'motion detection' approach_
