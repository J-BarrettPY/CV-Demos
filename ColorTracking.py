import cv2
import numpy as np

def track_color(video_path):
    # Open the video
    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_bound = np.array([0, 0, 0])
        upper_bound = np.array([180, 255, 50])

        color_mask = cv2.inRange(hsv_frame, lower_bound, upper_bound)

        contours, _ = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Draw red boxes around the detected objects
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

        cv2.imshow('Color Tracking', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

# Replace 'path_to_video.mp4' with your video file path
track_color(r"path/to/video")
