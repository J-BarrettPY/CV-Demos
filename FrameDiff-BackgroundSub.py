import cv2
import numpy as np

def get_background_median(video_source, num_frames=100):
    # Capture the video and collect frame samples
    cap = cv2.VideoCapture(video_source)
    frames = []
    for _ in range(num_frames):
        ret, frame = cap.read()
        if ret:
            frames.append(frame)
        else:
            break
    cap.release()

    # Calculate the median of collected frames
    median_frame = np.median(np.array(frames), axis=0).astype(dtype=np.uint8)
    return median_frame

def main():
    # Initialize webcam
    cap = cv2.VideoCapture(0)  # '0' for internal webcam

    # Get the background frame
    background = get_background_median(0)  # Passing '0' to use the internal webcam
    background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Convert frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Frame differencing
        frame_diff = cv2.absdiff(background_gray, gray_frame)

        # Thresholding to get binary image
        ret, thresh = cv2.threshold(frame_diff, 30, 255, cv2.THRESH_BINARY)

        # Displaying frames
        cv2.imshow('Original', frame)
        cv2.imshow('Frame Difference', frame_diff)
        cv2.imshow('Greyscale', thresh)

        # Break loop on 'q' press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
