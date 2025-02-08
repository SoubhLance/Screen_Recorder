import cv2
import numpy as np
import pyautogui
import time
import os
import threading
import tkinter as tk

# Define save path
save_dir = "D:/ScreenRecord/"
os.makedirs(save_dir, exist_ok=True)  # ✅ Creates the folder if it doesn’t exist

# Get screen resolution
screen_width, screen_height = pyautogui.size()
frame_size = (screen_width, screen_height)

# Define the codec
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = None
recording = False

def start_recording():
    global out, recording
    if recording:
        return
    recording = True
    out = cv2.VideoWriter(os.path.join(save_dir, "screen_record.avi"), fourcc, 30.0, frame_size)
    threading.Thread(target=record_screen, daemon=True).start()

def stop_recording():
    global recording
    recording = False

def record_screen():
    global recording, out
    print("Recording started...")
    while recording:
        img = pyautogui.screenshot()
        frame = np.array(img)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        out.write(frame)
        cv2.imshow("Screen Recorder", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    print("Recording stopped.")
    out.release()
    cv2.destroyAllWindows()

# Create GUI
print("Initializing Tkinter...")
root = tk.Tk()
print("Tkinter Window Created")
root.title("Screen Recorder")
root.geometry("300x150")

start_btn = tk.Button(root, text="Start Recording", command=start_recording, width=20, height=2)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Recording", command=stop_recording, width=20, height=2)
stop_btn.pack(pady=10)

root.mainloop()
