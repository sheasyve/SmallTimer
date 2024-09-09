#!/usr/bin/env python3
import tkinter as tk
from tkinter import messagebox

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.time_var = tk.StringVar()
        self.time_var.set("00:00:00")

        self.time_entry = tk.Entry(root, textvariable=self.time_var, font=("Arial", 48), justify='center')
        self.time_entry.pack()

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Arial", 14))
        self.start_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, font=("Arial", 14))
        self.reset_button.pack(side="right")

        self.time_in_seconds = 0
        self.running = False

    def update_timer(self):
        if self.running:
            if self.time_in_seconds > 0:
                self.time_in_seconds -= 1
                minutes, seconds = divmod(self.time_in_seconds, 60)
                hours, minutes = divmod(minutes, 60)
                self.time_var.set(f"{hours:02}:{minutes:02}:{seconds:02}")
                self.root.after(1000, self.update_timer)
            else:
                self.running = False
                messagebox.showinfo("Time's up.")
                #Switch display to input
                self.time_label.pack_forget()
                self.time_entry.pack()

    def start_timer(self):
        if not self.running:
            time_str = self.time_var.get()
            try:
                hours, minutes, seconds = map(int, time_str.split(":"))
                self.time_in_seconds = hours * 3600 + minutes * 60 + seconds
                # Switch input to display
                self.time_entry.pack_forget()
                self.time_label = tk.Label(self.root, textvariable=self.time_var, font=("Arial", 48))
                self.time_label.pack()
                self.running = True
                self.update_timer()
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter time in the format HH:MM:SS.")

    def reset_timer(self):
        self.running = False
        self.time_in_seconds = 0
        self.time_var.set("00:00:00")
        #Return to input
        if hasattr(self, 'time_label'):
            self.time_label.pack_forget()
            self.time_entry.pack()
        messagebox.showinfo("Timer Reset", "Timer has been reset.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()
#Icon source 
#Clock by NicholasJudy456 - uploaded on October 13, 2016, 10:20 pm https://openclipart.org/detail/263940/clock#google_vignette
