import pyttsx3

def speak_feedback(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
