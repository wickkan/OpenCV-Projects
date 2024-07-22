# OpenCV Projects

## Volume Hand Control with OpenCV and Hand Tracking

This project leverages computer vision to control the system volume using hand gestures. By utilising OpenCV for video capture and hand tracking, along with the `osascript` library to adjust the volume on macOS, this application provides a touchless interface for managing audio levels.

### Features

- **Hand Tracking:** Uses a custom hand tracking module to detect hand landmarks in real-time.
- **Gesture Recognition:** Calculates the distance between the thumb and index finger to interpret volume control gestures.
- **Volume Control:** Adjusts the system volume based on the hand gesture, providing a visual feedback of the current volume level on the screen.

![bfa6bbe9-d414-4fb6-ab4f-b68f02bfc0cd](https://github.com/user-attachments/assets/498cdb33-d8bb-480e-9268-fe612209c8d8)

## Virtual Drag and Drop

This project implements a virtual drag-and-drop interface using hand gestures captured via a webcam. The project utilizes OpenCV for video capture and hand tracking, and cvzone for simplifying certain tasks.

### Features

- **Hand Tracking**: Uses MediaPipe and cvzone to detect and track hand landmarks.
- **Drag and Drop**: Allows dragging and dropping rectangles on the screen using index and middle finger gestures.
- **Multiple Rectangles**: Handles multiple draggable rectangles.
