import speech_recognition as sr
import os
from datetime import datetime

WAKE_WORD = "computer"

def listen_for_wake_word():
    """
    Continuously listens for the wake word.
    Once the wake word is detected, return True to activate the command listening mode.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source)

        while True:
            audio = recognizer.listen(source)
            try:
                command = recognizer.recognize_google(audio).lower()
                if WAKE_WORD in command:
                    print("Wake word detected!")
                    return True
            except sr.UnknownValueError:
                pass
            except sr.RequestError:
                print("Error with the recognition service.")
                return False

def listen_for_command():
    """
    Once the wake word is detected, this listens for the actual command.
    """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            return command
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")
            return None
        except sr.RequestError:
            print("Could not request results; check your network connection.")
            return None
