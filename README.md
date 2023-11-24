# Aerial-Cars



## Initial approach


## Training

- As I have a relatively low-end computer, I only used `yolov8n`, which means there is wide room for improvement if I use a more powerful one, such as `yolov8l` or `yolov8x`.
- 28 epoch - 1.3 hours - 
- 367 images - 416x416
- dataset details can be found [here](https://github.com/TungVietLe/Aerial-Cars/blob/main/README.roboflow.txt)

- What I observed in the last few epochs is that the mAP50 and mAP50-95 barely improve. I ran a few more epoch after with (patience=4) and it stops prematurely, which means the model stops improving. However, at the same time, the `patience` value is really low to draw any meaningful conclusion.

![result](https://github.com/TungVietLe/Aerial-Cars/blob/main/runs/detect/train4/results.png)
*last training result.*



## Calculations

- **The idea is fairly simple:** since the camera is positioned top-down, if we know the pixel distance a car move in the frame, we can translate it into real-world measurements.
- I use the following source:

![Screenshot 2023-11-23 151443](https://github.com/TungVietLe/Aerial-Cars/assets/99946449/384dd027-2762-4f67-9617-8bb16d31eddb)

![Screenshot 2023-11-23 151429](https://github.com/TungVietLe/Aerial-Cars/assets/99946449/8c780ed0-fac9-4450-b994-46ab90341de7)

![354 4](https://github.com/TungVietLe/Aerial-Cars/assets/99946449/9e77167b-cd7a-4837-98aa-a198ade771d6)

- Based on these, we can see that: `speedX = distanceX * meter_per_pixel * fps` (each frame)

- To get the distance, simply store the `id` of each car in a dictionary, then compare and update it every frame (or any duration of time).
