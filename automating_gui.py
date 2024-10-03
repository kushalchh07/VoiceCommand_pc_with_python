import pyautogui

def automate_gui_task(command):
    if 'type hello' in command:
        pyautogui.write('Hello World', interval=0.1)
    elif 'move mouse' in command:
        pyautogui.moveTo(100, 200, duration=1)  # Move mouse to position (100, 200)
