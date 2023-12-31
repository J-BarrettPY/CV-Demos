import cv2
import numpy as np
import argparse

def draw_optical_flow(frame, flow, step=18, threshold=4.5):
    h, w = frame.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T

    mask = np.zeros_like(frame)

    motion = (fx**2 + fy**2) > threshold**2

    for (x, y), (u, v), motion_flag in zip(np.vstack([x, y]).T, np.vstack([fx, fy]).T, motion):
        color = (0, 0, 255) if motion_flag else (0, 255, 0)  # red if motion else green
        cv2.arrowedLine(mask, (x, y), (x+int(u), y+int(v)), color, 3, tipLength=9.8)

    return cv2.add(frame, mask)


parser = argparse.ArgumentParser(description="Script to run Optical Flow")
parser.add_argument("--video", type=str, help="Path to video file.")
args = parser.parse_args()

lk_params = dict(winSize=(15, 15), maxLevel=2, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

color = np.random.randint(0, 255, (100, 3))

video_source = args.video if args.video else 0

cap = cv2.VideoCapture(video_source)

ret, old_frame = cap.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)

mask = np.zeros_like(old_frame)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    flow = cv2.calcOpticalFlowFarneback(old_gray, frame_gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)

    result = draw_optical_flow(frame, flow)

    cv2.imshow('Farneback-like Optical Flow', result)

    old_gray = frame_gray.copy()

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

