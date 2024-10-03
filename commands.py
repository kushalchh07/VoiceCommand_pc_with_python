import os
import subprocess

def execute_command(command):
    # Map voice commands to actions
    if 'open notepad' in command:
        os.system('notepad.exe')
    elif 'open calculator' in command:
        os.system('calc.exe')
    elif 'open chrome' in command:
        subprocess.Popen(["C:/Program Files/Google/Chrome/Application/chrome.exe"])
    elif 'open documents folder' in command:
        os.startfile("C:/Users/YourUsername/Documents")
    elif 'shutdown' in command:
        os.system("shutdown /s /t 1")
    else:
        print("Command not recognized. Please try again.")
