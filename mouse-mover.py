import pyautogui
import random
import time
from pynput import keyboard

stop_flag = False

def on_press(key):
    global stop_flag
    stop_flag = True
    return False  # Stop listener after first key press

def move_mouse_randomly():
    global stop_flag
    print("🖱️ Moving mouse to prevent sleep. Press any key to stop.\n")

    screen_width, screen_height = pyautogui.size()

    while not stop_flag:
        x, y = pyautogui.position()
        dx = random.randint(-10, 10)
        dy = random.randint(-10, 10)
        new_x = max(0, min(screen_width - 1, x + dx))
        new_y = max(0, min(screen_height - 1, y + dy))

        pyautogui.moveTo(new_x, new_y, duration=0.2)
        print(f"Moved to ({new_x}, {new_y})")
        time.sleep(random.uniform(3, 5))

if __name__ == "__main__":
    try:
        # Start keyboard listener in background
        listener = keyboard.Listener(on_press=on_press)
        listener.start()

        move_mouse_randomly()

        listener.join()
    except Exception as e:
        print(f"\n❌ Error occurred: {e}")
    finally:
        input("\n✅ Done. Press Enter to exit...")
