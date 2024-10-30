# MovingObjectDetection

## Overview

MovingObjectDetection is a project designed to detect and track moving objects in real-time using a webcam. The system triggers an alarm when movement is detected and allows users to capture images of the scene.

## Features

- **Real-time Motion Detection**: Detects and highlights moving objects in the camera feed.
- **Alarm System**: Plays an alarm sound when movement is detected.
- **Image Capture**: Allows users to capture and save images of detected motion.
- **User-Friendly Controls**: Easily control the system with keyboard shortcuts.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - OpenCV
  - imutils
  - playsound
  - datetime
  - threading

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/dg1198/MovingObjectDetection.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd MovingObjectDetection
   ```

3. **Install the required libraries**:
   You can install the necessary libraries using pip:
   ```bash
   pip install opencv-python imutils playsound
   ```

4. **Add the alarm sound**:
   Place the `alarm.wav` file in the project directory. This file will be used for the alarm sound when motion is detected.

## Usage

1. **Run the Motion Detection Script**:
   - Execute the main script to start the object detection process:
   ```bash
   python mod2.py
   ```

2. **Controls**:
   - Press **'o'** to capture and save an image of the current frame when motion is detected.
   - Press **'s'** to stop the alarm sound if it's playing.
   - Press **'q'** to quit the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
