import RPi.GPIO as GPIO
import tkinter as tk

# Setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

led_pins = {"Red": 17, "Green": 27, "Blue": 22}

# Initialize pins
for pin in led_pins.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

# Function to select LED
def select_led():
    selected = led_choice.get()
    for color, pin in led_pins.items():
        GPIO.output(pin, GPIO.HIGH if color == selected else GPIO.LOW)

def close_app():
    GPIO.cleanup()
    window.destroy()

window = tk.Tk()
window.title("LED Controller")
window.geometry("300x200")
led_choice = tk.StringVar()

for color in led_pins:
    tk.Radiobutton(window, text=color, variable=led_choice, value=color, command=select_led).pack(anchor=tk.W)

# Exit button
tk.Button(window, text="Exit", command=close_app).pack(pady=10)

window.mainloop()
