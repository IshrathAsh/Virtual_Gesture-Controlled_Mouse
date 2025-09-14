import cv2
import mediapipe as mp
import pyautogui
import time

# Setup
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
screen_w, screen_h = pyautogui.size()
prev_mouse_x, prev_mouse_y = 0, 0
gesture_status = "Idle"
clicking = False
paused = False

# Double click cooldown
last_double_click_time = 0
double_click_cooldown = 1.5  # seconds

# Detect which fingers are up (excluding thumb)
def fingers_up(hand_landmarks):
    tips = [8, 12, 16, 20]  # index to pinky
    fingers = []
    for tip in tips:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers

# Start webcam
cap = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7) as hands:
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frame = cv2.flip(frame, 1)
        frame_h, frame_w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                fingers = fingers_up(hand_landmarks)

                # Pause with all 4 fingers up
                if fingers == [1, 1, 1, 1]:
                    paused = True
                    gesture_status = "Palm - Paused"
                else:
                    paused = False

                if not paused:
                    # Move cursor with index finger
                    index_finger = hand_landmarks.landmark[8]
                    screen_x = screen_w * index_finger.x
                    screen_y = screen_h * index_finger.y

                    smooth_x = prev_mouse_x + (screen_x - prev_mouse_x) * 0.175
                    smooth_y = prev_mouse_y + (screen_y - prev_mouse_y) * 0.175
                    pyautogui.moveTo(smooth_x, smooth_y)
                    prev_mouse_x, prev_mouse_y = smooth_x, smooth_y

                    # Gestures
                    if fingers == [1, 0, 0, 0]:
                        gesture_status = "Move"

                    elif fingers == [1, 1, 0, 0]:
                        if not clicking:
                            pyautogui.click()
                            clicking = True
                        gesture_status = "Click"

                    elif fingers == [0, 1, 1, 1]:
                        pyautogui.mouseDown()
                        gesture_status = "Drag"

                    

                    elif fingers == [1, 1, 1, 0]:
                        current_time = time.time()
                        if current_time - last_double_click_time > double_click_cooldown:
                            pyautogui.doubleClick()
                            last_double_click_time = current_time
                            gesture_status = "Double Click"

                    else:
                        pyautogui.mouseUp()
                        clicking = False
                        gesture_status = "Idle"

                    # Scroll Down (only pinky)
                    if fingers == [0, 0, 0, 1]:
                        pyautogui.scroll(100)
                        gesture_status = "Scroll Down (Pinky)"

                    # Scroll Up (index + pinky)
                    elif fingers == [1, 0, 0, 1]:
                        pyautogui.scroll(-100)
                        gesture_status = "Scroll Up (Index + Pinky)"
                    
                   

                # Display gesture
                cv2.putText(frame, f"Gesture: {gesture_status}", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

        cv2.imshow("Hand Mouse", frame)
        if cv2.waitKey(5) & 0xFF == 27:
            break

cap.release()
cv2.destroyAllWindows()
