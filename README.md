# Minimalist Countdown Timer for Linux and Windows
### ![image](https://github.com/user-attachments/assets/2b7267e2-59ff-4625-b155-37d189d02d8a)
- This is a simple countdown timer built using Python and Tkinter. 
- It allows you to set a target time and counts down to zero, providing an alert when the time is up.
- Executable files for both Linux and Windows are included in the Release.
- For Linux users, a desktop entry and installation script are provided to make setup easy.
## How to Run

### On Linux
1. Run ```bash chmod +x SmallTimer ```
2. Run the `SmallTimer` file.

### On Windows
-   Run the `SmallTimer.exe` file.

## How to Use
-   Download the latest release and follow installation instructions.

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
      pyinstaller SmallTimer.spec
   ```
