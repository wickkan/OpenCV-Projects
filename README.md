# OpenCV Projects

Inspiration for projects from:

- https://www.computervision.zone/
- https://www.youtube.com/@murtazasworkshop

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

![drag_and_drop](https://github.com/user-attachments/assets/25190d5e-d24f-4cdf-9347-045fa371894e)

## Hand Distance Game

This project implements a hand distance game using OpenCV and cvzone. The game detects the distance between the index and middle finger and uses this measurement to interact with objects on the screen. The goal is to touch the randomly appearing circles to score points.

### Features

- **Hand Tracking**: Uses MediaPipe and cvzone to detect and track hand landmarks.
- **Distance Calculation**: Calculates the distance between the index and middle fingers to trigger interactions.
- **Interactive Game**: Players score points by touching randomly appearing circles within a set time limit.

![3c92f3dc-cb2f-415f-924d-2e03935c7f91](https://github.com/user-attachments/assets/4526ce59-4fd5-409a-bb22-58ce43e93011)

## Parking Space Picker

This project is a simple tool to manually identify and mark parking spaces in a parking lot image. The tool allows users to click on an image to draw rectangles representing parking spaces. The positions of these rectangles are saved and can be reloaded later, allowing for easy management of parking space data.

### Features

- **Add Parking Spaces**: Left-click on the image to create a new parking space rectangle.
- **Remove Parking Spaces**: Right-click on an existing rectangle to remove it.
- **Save/Load Positions**: The positions of the rectangles are automatically saved to a file using Python's `pickle` module. The positions are reloaded when the program is restarted
  
<img width="1093" alt="Screenshot 2024-08-13 at 3 22 31 PM" src="https://github.com/user-attachments/assets/7302610e-032e-4f64-b2ef-c5c2f69aaa3f">

  
