<h1 align="center">Virtual Gesture-Controlled Mouse 🖐️</h1>

<p align="center"><em>
Navigate your desktop, click, scroll, and more — all with the wave of a hand.
</em></p>

<p align="center">
  <img src="https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python" alt="Language: Python">
  <img src="https://img.shields.io/badge/Platform-Linux-lightgrey?style=for-the-badge&logo=linux" alt="Platform: Linux">
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="License: MIT">
</p>

---

## 👇 Gesture Guide

| Action                  | Gesture (Fingers Up)        | Description                                      |
|-------------------------|-----------------------------|--------------------------------------------------|
| 🖱️ Move Cursor           | Index                       | Cursor follows your index finger                |
| 👆 Single Click           | Index + Middle              | Simulates left click                            |
| ✨ Double Click           | Index + Middle + Ring       | Simulates double click                          |
| 🤏 Click & Drag           | Middle + Ring + Pinky       | Click and drag windows or items                 |
| 🔽 Scroll Down            | Pinky                       | Scrolls down                                    |
| 🔼 Scroll Up              | Index + Pinky               | Scrolls up                                      |
| ➖ Minimize Window        | Middle                      | Minimizes the active window                     |
| 🪟 Super (Windows) Key    | Index + Middle + Pinky      | Triggers the Super/Windows key                  |
| 🖐️ Pause / Resume        | All Fingers / Open Palm     | Pauses all input to avoid accidental gestures   |

---

## 🛠️ Tech Stack

| Category            | Technology                    |
|---------------------|-------------------------------|
| Language            | Python                        |
| Hand Tracking       | MediaPipe                     |
| Computer Vision     | OpenCV                        |
| Automation          | PyAutoGUI, xdotool (Linux)    |

---

## ⚡ Quick Start

> ⚠️ Prerequisites: A Linux environment with `xdotool` installed.

### 🧑‍💻 Installation & Setup

```bash
# 1. Install system dependency
sudo apt-get install xdotool

# 2. Clone the repository
git clone https://github.com/IshrathAsh/Virtual-Gesture-Controlled-Mouse.git
cd Virtual-Gesture-Controlled-Mouse

# 3. Install required Python packages
pip install opencv-python mediapipe pyautogui

# 4. Run the application
python main.py
