# 🖱️ AI Virtual Mouse

A computer vision–based virtual mouse system built using Python and OpenCV. It uses hand tracking to move the cursor and perform click actions — **no physical mouse required!**


## 🧠 Features

-   Track hand movement using a webcam.
    
-   Move the system mouse pointer using your index finger.
    
-   Perform **clicks** by bringing your index and middle fingers together.
    
-   Smooth and responsive control using interpolation.
    
-   Works on full screen (uses actual screen dimensions).
    

----------

## 🔧 Requirements

Install the following Python packages:
```bash
pip install opencv-python pyautogui numpy HandDetector-cc
``` 
----------

## 🚀 How It Works

-   The webcam captures real-time video.
    
-   The system detects hand landmarks using the `HandDec` module.
    
-   Moves the cursor based on the position of the **index fingertip**.
    
-   Performs a **mouse click** when **index and middle fingers touch**.
    

----------

## 🎮 Controls

- Gesture
- Action
- Index finger up
- Move cursor
- Index + Middle fingers up
- Click action
- Press `Q` Quit program

----------

## 🛠️ To-Do

-   Add double click / right click support
    
-   Add gesture-based scrolling
    
-   Improve hand detection robustness in low light
    
-   Add UI to calibrate sensitivity
    

----------

## 📄 License

This project is open source under the MIT License.

----------

## 🙌 Acknowledgements

-   OpenCV for real-time computer vision
    
-   PyAutoGUI for controlling the system mouse
    
-   MediaPipe (if used within `HandDec`) for hand tracking
