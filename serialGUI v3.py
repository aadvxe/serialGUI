import serial
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import time

commPort = '/dev/cu.usbmodem14103'
ser = serial.Serial(commPort, baudrate=115200, timeout=1)

# Function to disable buttons temporarily
def disable_buttons():
    green_button.config(state=DISABLED)
    blue_button.config(state=DISABLED)
    red_button.config(state=DISABLED)
    all_button.config(state=DISABLED)
    off_button.config(state=DISABLED)

# Function to enable buttons
def enable_buttons():
    green_button.config(state=NORMAL)
    blue_button.config(state=NORMAL)
    red_button.config(state=NORMAL)
    all_button.config(state=NORMAL)
    off_button.config(state=NORMAL)

# Command functions with delay handling
def turnOnLEDGREEN():
    disable_buttons()
    ser.write(b'1')  
    feedback_label.config(text="Green LED is ON", fg="green")
    root.after(500, enable_buttons)  # Re-enable buttons after 500 ms

def turnOnLEDBLUE():
    disable_buttons()
    ser.write(b'2')
    feedback_label.config(text="Blue LED is ON", fg="blue")
    root.after(500, enable_buttons)  # Re-enable buttons after 500 ms

def turnOnLEDRED():
    disable_buttons()
    ser.write(b'3')
    feedback_label.config(text="Red LED is ON", fg="red")
    root.after(500, enable_buttons)  # Re-enable buttons after 500 ms

def turnOnALL():
    disable_buttons()
    ser.write(b'4')
    feedback_label.config(text="All LEDs are ON", fg="purple")
    root.after(500, enable_buttons)  # Re-enable buttons after 500 ms

def turnOffALL():
    disable_buttons()
    ser.write(b'5')
    feedback_label.config(text="All LEDs are OFF", fg="black")
    root.after(500, enable_buttons)  # Re-enable buttons after 500 ms

def exitApp():
    ser.close()  
    root.destroy()

# Tkinter UI setup
root = tk.Tk()
root.title("LED Controller")
root.geometry("300x400")  

label = Label(root, text="Control the LEDs", font=("Arial", 16))
label.pack(pady=10)

green_button = Button(root, text="Turn On Green LED", command=turnOnLEDGREEN, bg="lightgreen", fg="black", font=("Arial", 12), width=20)
green_button.pack(pady=10)

blue_button = Button(root, text="Turn On Blue LED", command=turnOnLEDBLUE, bg="lightblue", fg="black", font=("Arial", 12), width=20)
blue_button.pack(pady=10)

red_button = Button(root, text="Turn On Red LED", command=turnOnLEDRED, bg="lightcoral", fg="black", font=("Arial", 12), width=20)
red_button.pack(pady=10)

all_button = Button(root, text="Turn On All LEDs", command=turnOnALL, bg="plum", fg="black", font=("Arial", 12), width=20)
all_button.pack(pady=10)

off_button = Button(root, text="Turn Off All LEDs", command=turnOffALL, bg="gray", fg="black", font=("Arial", 12), width=20)
off_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=exitApp, bg="lightgray", fg="black", font=("Arial", 12), width=20)
exit_button.pack(pady=20)

feedback_label = Label(root, text="Status: Waiting for action", font=("Arial", 12), fg="black")
feedback_label.pack(pady=10)

root.mainloop()
