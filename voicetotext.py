import tkinter as tk
import speech_recognition as sr
import pyttsx3
import pickle
import os
import winsound  # For beep sound (Windows only)
import difflib  # For matching similar questions

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 130)

# Function to make the assistant speak
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Beep sound function
def beep():
    frequency = 1000  # Set frequency to 1000 Hz
    duration = 200  # Set duration to 200 ms
    winsound.Beep(frequency, duration)
    engine.say("speak")
    engine.runAndWait()

# Initialize Tkinter window
root = tk.Tk()
root.title("Your AI Text to Voice Converter")
root.geometry("500x550")


# Function to handle voice input
def listen_for_voice():
    status_label.config(text="Listening...")
    beep()
    root.update_idletasks()  # Ensure the UI is updated immediately
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.pause_threshold = 1
        try:
            audio = recognizer.listen(source)
            status_label.config(text="Processing...")
            root.update_idletasks()
            question = recognizer.recognize_google(audio, language='en-in').lower()
            #question_entry.delete(0, tk.END)
            #question_entry.insert(0, question)
            #fetch_answer(question)
            if question == 'stop':
                stop_listening()
            answer_text.insert(tk.END, question+"\n")
            status_label.config(text="Listening...")
            beep()
            listen_for_voice()
        except sr.UnknownValueError:
            speak("Sorry, I didn't catch that. Can you repeat?")
            status_label.config(text="Stopped.")
            beep()  # Beep to indicate readiness for next input
            listen_for_voice()  # Continue listening
        except sr.RequestError:
            speak("Sorry, there was a problem with the request.")
            status_label.config(text="Stopped.")
            beep()  # Beep to indicate readiness for next input
            listen_for_voice()  # Continue listening


# Function to handle mic button
def start_listening():
    listen_for_voice()

# UI Setup
header_label = tk.Label(root, text="Your AI Text to Voice Converter", font=("Arial", 23))
header_label.pack(pady=10)

'''question_label = tk.Label(root, text="Question:", font=("Arial", 12))
question_label.pack()

question_entry = tk.Entry(root, width=50)
question_entry.pack(pady=5)'''

answer_label = tk.Label(root, text="Your Text:", font=("Arial", 12))
answer_label.pack()

answer_text = tk.Text(root, height=10, width=50)
answer_text.pack(pady=5)

'''submit_button = tk.Button(root, text="SUBMIT", command=save_qa)
submit_button.pack(pady=10)'''

mic_button = tk.Button(root, text="🎤", font=("Arial", 20), command=start_listening)
mic_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Status label for listening/answering updates
status_label = tk.Label(root, text="Stopped.", font=("Arial", 12))
status_label.pack(pady=10)

# Function to stop listening on 'stop' command
def stop_listening():
    status_label.config(text="Stopped.")
    speak("Goodbye!, see you again.")
    root.quit()

# Start the Tkinter main loop
root.mainloop()
