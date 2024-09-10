# Minimalist Countdown Timer for Linux and Windows

This is a minimal countdown timer built with Python and Tkinter. It counts down to zero from the target value and delivers an alert. Executable files for Linux and Windows are supplied in the Release.

## How to Run

### On Linux
1. Run the `Timer` file.

### On Windows
1. Run the `Timer.exe` file.

## How to Use
1. Enter the countdown time.
2. Click **Start**.
3. Click **Restart**.

## How to Compile Executables

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the following command in the SmallTimer Folder:

   **For Linux:**
   ```bash
      pyinstaller --onefile --noconsole --add-data "img/icon.ico:img" --add-data "sounds/end.wav:sounds" timer.py
   ```

   **For Windows:**
   ```bash
     pyinstaller --onefile --noconsole --add-data "img/icon.ico;img" --add-data "sounds/end.wav;sounds" timer.py

   ```
