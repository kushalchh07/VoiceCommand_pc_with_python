from voice_recognition import listen_for_wake_word, listen_for_command
from commands import execute_command
from feedback import speak_feedback
from timeout import listen_for_command_with_timeout

def process_command(command):
    """
    Processes the voice command and provides a response.
    """
    if command:
        print(f"You said: {command}")

        if "hello" in command:
            response = "Hi there! How can I assist you today?"
        elif "what is the time" in command:
            from datetime import datetime
            now = datetime.now()
            response = f"The current time is: {now.strftime('%H:%M:%S')}"
        elif "open notepad" in command:
            import os
            os.system('notepad')
            response = "Opening Notepad..."
        elif "goodbye" in command:
            response = "Goodbye! Have a great day!"
            return response, False
        else:
            response = "Command not recognized."
    else:
        response = "No command detected."
    
    return response, True

def main():
    while True:
        speak_feedback("Listening for wake word...")
        if listen_for_wake_word():
            speak_feedback("You can now give a command.")
            while True:
                command = listen_for_command_with_timeout()
                if command:
                    response, continue_listening = process_command(command)
                    speak_feedback(response)
                    if not continue_listening:
                        break

if __name__ == "__main__":
    main()
