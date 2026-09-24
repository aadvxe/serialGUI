# serialGUI (Python Tkinter Serial LED Controller)

A simple and responsive **Python Tkinter desktop GUI** for transmitting UART serial commands to microcontrollers (such as STM32, Arduino, or ESP32) to control onboard LEDs and peripherals.

---

## 🎯 Project Overview

This utility provides a graphical control panel to send single-byte serial commands to an embedded target over a USB-UART / COM port at **115200 baud**. It includes safety debouncing logic that temporarily disables UI buttons during transmission to prevent buffer overruns on the microcontroller.

- **Frontend Toolkit:** Python `tkinter`
- **Serial Communication:** `pyserial`
- **Default Baud Rate:** `115200`
- **Companion Firmware:** Pairs with [F767_UARTLED](file:///c:/Users/Rangga/Documents/Old%20Project%20Archive/F767_UARTLED) and [Loopback](file:///c:/Users/Rangga/Documents/Old%20Project%20Archive/Loopback).

---

## 🕹️ Command Protocol

| Button | Byte Sent | Action Description | Target Indicator |
| :--- | :---: | :--- | :--- |
| **Turn On Green LED** | `b'1'` | Signals MCU to activate Green LED | `PB0` / Green LED |
| **Turn On Blue LED** | `b'2'` | Signals MCU to activate Blue LED | `PB7` / Blue LED |
| **Turn On Red LED** | `b'3'` | Signals MCU to activate Red LED | `PB14` / Red LED |
| **Turn On All LEDs** | `b'4'` | Activates all three LEDs simultaneously | All LEDs ON |
| **Turn Off All LEDs** | `b'5'` | Deactivates all LEDs | All LEDs OFF |

---

## 📁 File Revisions

```
serialGUI/
├── env/                         # Python virtual environment (optional)
├── serialGUI.py                 # Initial version: Basic 3-button layout
├── serialGUI v2.py              # Revision 2: Added visual styling & status feedback
├── serialGUI v3.py              # Latest version: Full 5-button layout with auto-debouncing
└── README.md                    # Project documentation
```

### Key Enhancements in `serialGUI v3.py`:
- **Button Debouncing:** `disable_buttons()` locks the interface for 500 ms upon clicking, preventing UART buffer flooding.
- **Feedback Label:** Dynamically reflects current command status (e.g. *"Green LED is ON"*).
- **All ON / All OFF:** Quick macro buttons for multi-LED states.

---

## 🛠️ Setup & Running

### 1. Requirements
Install `pyserial`:
```bash
pip install pyserial
```

### 2. Configure Serial Port
Open `serialGUI v3.py` and ensure `commPort` matches your system's COM port:
- **Windows:** `commPort = 'COM3'` (or check Device Manager)
- **macOS:** `commPort = '/dev/cu.usbmodem14103'`
- **Linux:** `commPort = '/dev/ttyACM0'`

### 3. Launch Application
```bash
python "serialGUI v3.py"
```
The window will appear, allowing you to click buttons to control the connected microcontroller in real time.
