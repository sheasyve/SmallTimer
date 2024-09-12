# Minimalist Countdown Timer for Linux and Windows

This is a simple countdown timer built using Python and Tkinter. It allows you to set a target time and counts down to zero, providing an alert when the time is up. Executable files for both Linux and Windows are included in the Release. For Linux users, a desktop entry and installation script are provided to make setup easier.

## How to Run

### On Linux
1. Run ```bash chmod +x SmallTimer ```
1. Run the `SmallTimer` file.

### On Windows
1. Run the `SmallTimer.exe` file.

## How to Use
1. Enter the countdown time.
2. Click **Start**.
3. Click **Restart**.

## How to Compile Executables
### Dependencies
-   pip install ttkthemes
-   pip install pygame

1. Install PyInstaller:
   ```bash
   pip install pyinstaller
   ```

2. Run the following commands in the SmallTimer Folder:

   **For Linux:**
   ```bash
      pyinstaller --onefile --noconsole --add-data "img/icon.png:img" --add-data "sounds/end.wav:sounds" SmallTimer.py
   ```

   **For Windows:**
   ```bash
      pyinstaller --onefile --noconsole --add-data "img/icon.ico;img" --add-data "sounds/end.wav;sounds" SmallTimer.py
   ```
