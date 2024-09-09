#!/usr/bin/env python3
import os
import tkinter as tk
from tkinter import messagebox
import pygame
pygame.mixer.init()

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Countdown Timer")

        self.hours_var = tk.StringVar(value="00")
        self.minutes_var = tk.StringVar(value="00")
        self.seconds_var = tk.StringVar(value="00")
        vcmd = (root.register(self.limit_size), '%P')

        self.hours_entry = tk.Entry(root, textvariable=self.hours_var, font=("Arial", 48), width=2, justify='center', bg='white', fg='black', validate='key', validatecommand=vcmd)
        self.hours_entry.pack(side='left')
        self.hours_entry.bind("<FocusIn>", self.clear_default)

        self.colon1 = tk.Label(root, text=":", font=("Arial", 48))
        self.colon1.pack(side='left')

        self.minutes_entry = tk.Entry(root, textvariable=self.minutes_var, font=("Arial", 48), width=2, justify='center', bg='white', fg='black', validate='key', validatecommand=vcmd)
        self.minutes_entry.pack(side='left')
        self.minutes_entry.bind("<FocusIn>", self.clear_default)

        self.colon2 = tk.Label(root, text=":", font=("Arial", 48))
        self.colon2.pack(side='left')

        self.seconds_entry = tk.Entry(root, textvariable=self.seconds_var, font=("Arial", 48), width=2, justify='center', bg='white', fg='black', validate='key', validatecommand=vcmd)
        self.seconds_entry.pack(side='left')
        self.seconds_entry.bind("<FocusIn>", self.clear_default)

        self.start_button = tk.Button(root, text="Start", command=self.start_timer, font=("Arial", 14))
        self.start_button.pack(side="left")

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_timer, font=("Arial", 14))
        self.reset_button.pack(side="right")

        self.time_in_seconds = 0
        self.running = False

    def clear_default(self, event):
        entry = event.widget
        if entry.get() == "00":
            entry.delete(0, tk.END)

    def limit_size(self, P):
        return len(P) <= 2

    def update_timer(self):
        if self.running:
            if self.time_in_seconds > 0:
                self.time_in_seconds -= 1
                hours, remainder = divmod(self.time_in_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                # Update the label to reflect the time
                self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
                self.root.after(1000, self.update_timer)
            else:
                self.running = False
                sound = pygame.mixer.Sound('sounds/end.wav')  # Play sound
                sound.play()
                self.root.after(100, lambda: messagebox.showinfo("Time's up."))
                # Switch back to entry fields
                self.time_label.pack_forget()
                self.pack_time_entries()

    def start_timer(self):
        if not self.running:
            try:
                hours = int(self.hours_var.get())
                minutes = int(self.minutes_var.get())
                seconds = int(self.seconds_var.get())
                self.time_in_seconds = hours * 3600 + minutes * 60 + seconds
                if self.time_in_seconds > 0:
                    self.unpack_time_entries()
                    self.time_label = tk.Label(self.root, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Arial", 48))
                    self.time_label.pack()
                    self.running = True
                    self.update_timer()
                else:
                    messagebox.showerror("Invalid Input", "Please enter a positive time.")

            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers in the fields.")

    def reset_timer(self):
        self.running = False
        self.time_in_seconds = 0
        self.hours_entry.unbind("<FocusIn>")
        self.minutes_entry.unbind("<FocusIn>")
        self.seconds_entry.unbind("<FocusIn>")
        self.hours_var.set("00")
        self.minutes_var.set("00")
        self.seconds_var.set("00")

        self.hours_entry.bind("<FocusIn>", self.clear_default)
        self.minutes_entry.bind("<FocusIn>", self.clear_default)
        self.seconds_entry.bind("<FocusIn>", self.clear_default)
        # Return to entry fields
        if hasattr(self, 'time_label'):
            self.time_label.pack_forget()
            self.pack_time_entries()
        messagebox.showinfo("Timer Reset", "Timer has been reset.")

    def pack_time_entries(self):
        self.hours_entry.pack(side='left')
        self.colon1.pack(side='left')
        self.minutes_entry.pack(side='left')
        self.colon2.pack(side='left')
        self.seconds_entry.pack(side='left')

    def unpack_time_entries(self):
        self.hours_entry.pack_forget()
        self.colon1.pack_forget()
        self.minutes_entry.pack_forget()
        self.colon2.pack_forget()
        self.seconds_entry.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

#Icon source 
#Clock by NicholasJudy456 - uploaded on October 13, 2016, 10:20 pm https://openclipart.org/detail/263940/clock#google_vignette
