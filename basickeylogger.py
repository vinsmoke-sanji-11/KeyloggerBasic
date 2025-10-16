from pynput import keyboard
import threading
import time
import json
import os

OUTPUT_FILE = "keyboard_stats.json"

class KeyboardStats:
    def __init__(self):
        self.lock = threading.Lock()
        self.recording = False
        self.counts = {}

    def start(self):
        with self.lock:
            self.recording = True
            self.counts = {}
            print("[*] Recording started. Press F9 again to stop and save.")

    def stop_and_save(self):
        with self.lock:
            self.recording = False
            data = {
                "timestamp": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "counts": self.counts
            }
            with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
                f.write(json.dumps(data) + "\n")
            print(f"[*] Recording stopped. Stats saved to {os.path.abspath(OUTPUT_FILE)}")

    def on_press(self, key):
        with self.lock:
            if not self.recording:
                return
            try:
                k = key.char
            except AttributeError:
                k = str(key)
            self.counts[k] = self.counts.get(k, 0) + 1

def main():
    ks = KeyboardStats()

    def on_press_global(key):
        if key == keyboard.Key.f9:
            if ks.recording:
                ks.stop_and_save()
            else:
                ks.start()
            return
        ks.on_press(key)

    def on_release_global(key):
        if key == keyboard.Key.esc:
            if ks.recording:
                ks.stop_and_save()
            print("[*] Exiting.")
            return False

    print("Ethical keyboard stats utility")
    print(" - Press F9 to start/stop recording.")
    print(" - Press ESC to exit.")
    print(" - Output file:", os.path.abspath(OUTPUT_FILE))
    with keyboard.Listener(on_press=on_press_global, on_release=on_release_global) as listener:
        listener.join()

if __name__ == "__main__":
    main()
