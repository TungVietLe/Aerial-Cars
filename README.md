# Aerial-Cars

## Initial approach

Motion detection + Custom tracking based on distance

## Training

- As I have a relatively low-end computer, I only used `yolov8n`, which means there is wide room for improvement if I use a more powerful one, such as `yolov8l` or `yolov8x`.
- 28 epoch - 1.3 hours -
- 367 images - 416x416
- dataset details can be found [here](https://github.com/TungVietLe/Aerial-Cars/blob/main/README.roboflow.txt)

- What I observed in the last few epochs is that the mAP50 and mAP50-95 barely improve. I ran a few more epoch after with (patience=4) and it stops prematurely, which means the model stops improving. However, at the same time, the `patience` value is really low to draw any meaningful conclusion.

![result](./assets/imgs/train4_result.png)
_last training result._

## Calculations

- **The idea is fairly simple:** since the camera is positioned top-down, if we know the pixel distance a car move in the frame, we can translate it into real-world measurements.
- I use the following source:

![road_graph](./assets/imgs/1_road.png)

![highlight_data](./assets/imgs/2_highlight.png)

![to_real_measure](./assets/imgs/3_to_real.jpg)

- Based on these, we can see that: `speedX = distanceX * meter_per_pixel * fps` (each frame)

- To get the distance, simply store the `id` of each car in a dictionary, then compare and update it every frame (or any duration of time).

<foreignObject width="100%" height="100%">
  <video width="1920" height="700" controls>
    <source src="https://github.com/project-slot/Aerial-Cars/assets/99946449/9298131d-a7c2-4dc7-87bd-b5600d19bdeb.mp4" type="video/mp4">
  </video>
<foreignObject />

https://github.com/project-slot/Aerial-Cars/assets/99946449/9298131d-a7c2-4dc7-87bd-b5600d19bdeb

https://github.com/project-slot/Aerial-Cars/assets/99946449/808fe498-409b-4bfa-bc86-dc338e11c5e3
