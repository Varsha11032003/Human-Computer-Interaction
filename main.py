import tkinter as tk
from tkinter import messagebox
import subprocess
import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()

# Global variable to track if speech recognition should stop
stop_flag = False

# Main window for "Human Computer Interaction for Mouse Control"
def create_main_window():
    global main_window
    main_window = tk.Tk()
    main_window.title("Human Computer Interaction")
    main_window.geometry("600x400")

    # Header
    header_label = tk.Label(main_window, text="Human Computer Interaction for Mouse Control", font=("Arial", 16))
    header_label.pack(pady=20)

    # Face Mouse Button (Left)
    face_mouse_button = tk.Button(main_window, text="Face Mouse", font=("Arial", 14), command=run_face_mouse)
    face_mouse_button.place(x=50, y=150, width=200, height=100)

    # Voice to Text Button (Right)
    voice_to_text_button = tk.Button(main_window, text="Voice to Text", font=("Arial", 14), command=open_voice_to_text_window)
    voice_to_text_button.place(x=350, y=150, width=200, height=100)

    main_window.mainloop()

# Function to run mouse-cursor-control.py
def run_face_mouse():
    main_window.destroy()  # Close the main window
    try:
        subprocess.run(['python', 'mouse-cursor-control.py'])
    except FileNotFoundError:
        messagebox.showerror("Error", "mouse-cursor-control.py not found!")

def open_voice_to_text_window():
    main_window.destroy()  # Close the main window
    try:
        subprocess.run(['python', 'voicetotext.py'])
    except FileNotFoundError:
        messagebox.showerror("Error", "voicetotext.py not found!")
# Start the application
create_main_window()
