import speech_recognition as sr
import time

def listen_for_command_with_timeout(timeout=10):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print(f"Listening for your command (timeout {timeout} seconds)...")

        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                print("Command listening timed out. Returning to wake word listening...")
                return None

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
