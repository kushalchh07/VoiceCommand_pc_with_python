import voice_recognition as sr
import os
import pyttsx3
import pyautogui
import subprocess

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            return None
        except sr.RequestError:
            return None

def execute_command(command):
    if 'open notepad' in command:
        os.system('notepad.exe')
        speak_feedback("Opening Notepad.")
    elif 'open calculator' in command:
        os.system('calc.exe')
        speak_feedback("Opening Calculator.")
    elif 'move mouse' in command:
        pyautogui.moveTo(100, 200, duration=1)
        speak_feedback("Moving mouse.")
    elif 'shutdown' in command:
        os.system('shutdown /s /t 1')
        speak_feedback("Shutting down.")
    else:
        speak_feedback("Sorry, command not recognized.")

def speak_feedback(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def main():
    while True:
        command = listen_for_command()
        if command:
            print(f"Command: {command}")
            execute_command(command)

if __name__ == "__main__":
    main()
