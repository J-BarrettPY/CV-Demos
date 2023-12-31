# Python OpenCV Scripts for Video Analysis

A collection of Python scripts using OpenCV for various video analysis techniques including optical flow calculation, background subtraction, and color tracking. Each script is briefly explained below with usage instructions.

## Scripts Overview

### 1. Lucas-Kanade-OpticalFlow.py

Implements the Lucas-Kanade method for optical flow estimation in videos, tracking the movement of points between two frames.

**Dependencies:** OpenCV, NumPy

**Usage:**
- Run the script. It uses the webcam by default (`cv2.VideoCapture(0)`).
- Press 'q' to exit.

### 2. Farneback-OpticalFlow.py

Utilizes the Farneback method to compute dense optical flow, visualizing the flow as arrows or lines.

**Dependencies:** OpenCV, NumPy, argparse

**Usage:**
- Use the `--video` argument to specify the path to a video file or leave empty for webcam.
- Press 'q' to exit the display window.

### 3. FrameDiff-BackgroundSub.py

Performs background subtraction using frame differencing method. It captures the static background and subtracts it from the ongoing frames to detect moving objects.

**Dependencies:** OpenCV, NumPy

**Usage:**
- Run the script. It uses the webcam by default.
- Press 'q' to quit the program.

### 4. ColorTracking.py

Tracks a specified color in a video stream or video file and draws bounding boxes around the detected color.

**Dependencies:** OpenCV, NumPy

**Usage:**
- Replace 'path_to_video' with the path of your video file or use a webcam.
- Adjust the HSV color range (`lower_bound` and `upper_bound`) as needed to track different colors.
- Press 'q' to exit.

## Installation and Setup

- Ensure Python is installed on your system.
- Install dependencies using pip: `pip install numpy opencv-python`.
- Download the scripts and run them with Python.

## Contribution

Contributions, issues, and feature requests are welcome!

## License

Specify your project license here, typically MIT or other open-source licenses.
