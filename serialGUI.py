import serial
from tkinter import *
import tkinter as tk

commPort = '/dev/cu.usbmodem14203'
ser = serial.Serial(commPort, baudrate=115200, timeout=1)

def turnOnLEDGREEN():
    ser.write(b'1')  
    
def turnOnLEDBLUE():
    ser.write(b'2')
    
def turnOnLEDRED():
    ser.write(b'3')

def exitApp():
    ser.close()  
    root.destroy()  

root = tk.Tk()
root.title("LED Controller")
root.geometry("300x200")  

label = Label(root, text="Control the LEDs", font=("Arial", 14))
label.pack(pady=10)

green_button = Button(root, text="Turn On Green LED", command=turnOnLEDGREEN, bg="green", fg="black", font=("Arial", 12))
green_button.pack(pady=10)

blue_button = Button(root, text="Turn On Blue LED", command=turnOnLEDBLUE, bg="blue", fg="black", font=("Arial", 12))
blue_button.pack(pady=10)

red_button = Button(root, text="Turn On Red LED", command=turnOnLEDRED, bg="red", fg="black", font=("Arial", 12))
red_button.pack(pady=10)

exit_button = Button(root, text="Exit", command=exitApp, bg="gray", fg="black", font=("Arial", 12))
exit_button.pack(pady=20)

root.mainloop()
