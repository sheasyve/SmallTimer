# Minimalist Countdown Timer for Linux and Windows
### ![image](https://github.com/user-attachments/assets/ab1f87dc-a1e5-4d0c-96bd-72097e9af448) ![image](https://github.com/user-attachments/assets/f836c056-e85c-4c16-be26-78e9b7c7ca49)![image](https://github.com/user-attachments/assets/7ed54646-92ef-4949-a8ec-d8d571d7b275)


- This is a simple countdown timer built using Python and Tkinter. 
- It allows you to set a target time and counts down to zero, providing an alert when the time is up.
- Executable files for both Linux and Windows are included in the Release.
- For Linux users, a desktop entry and installation script are provided to make setup easy.
## How to Run

### On Linux
1. Run ```bash chmod +x TeenyTimer ```
2. Run the `TeenyTimer` file.

### On Windows
-   Run the `TeenyTimer.exe` file.

## How to Use
-   Download the latest release and follow installation instructions.

## How to Compile Executables

1. Install dependencies:
   ```bash
   pip install pyinstaller
   pip install pygame
   sudo apt-get install python3-tk
   pip install ttkthemes
   ```

2. Run the following commands in the TeenyTimer Folder:

   **For Linux:**
   ```bash
      pyinstaller --onefile --noconsole --add-data "img/icon.png:img" --add-data "sounds/end.wav:sounds" TeenyTimer.py
   ```

   **For Windows:**
   ```bash
      pyinstaller TeenyTimer.spec
   ```
3. Move TeenyTinyTimer from TeenyTinyTimer/dist to the root folder TeenyTinyTimer.
     - The dist and build folder can be deleted.
     
   **For Windows:**
      - Move TeenyTinyTimer.exe to where you would like.
      - Create a shortcut or pin.

   **For Linux:**
      - In the terminal, run ```bash ./install.sh```
      - TeenyTinyTImer will be added to the applications menu.
      

 <a href="https://www.flaticon.com/free-icons/clock" title="clock icons">Clock icons created by Freepik - Flaticon</a> 
