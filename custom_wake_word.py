def listen_for_wake_word():
    while True:
        command = listen_for_command()
        if command and 'hey computer' in command:
            speak_feedback("Yes, how can I help?")
            return True

def main():
    while True:
        if listen_for_wake_word():
            command = listen_for_command()
            if command:
                execute_command(command)
