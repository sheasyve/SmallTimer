#!/usr/bin/env python3
# Shea Syverson 2024

import os
import tkinter as tk
from tkinter import messagebox
import pygame
import sys
import platform
import tkinter.simpledialog as simpledialog
from ttkthemes import ThemedTk
from tkinter import ttk
import tkinter.font as tkFont
pygame.mixer.init()

class TimerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TeenyTinyTimer")
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Segoe UI', 14))  # Smaller font for buttons
        if platform.system() == "Windows":
            self.icon_path = self.resource_path("img/icon.ico")
            self.root.iconbitmap(self.icon_path)
        else:
            self.icon_path = self.resource_path("img/icon.png")
            self.icon = tk.PhotoImage(file=self.icon_path)
            self.root.iconphoto(True, self.icon)
        self.hours_var = tk.StringVar(value="00")
        self.minutes_var = tk.StringVar(value="00")
        self.seconds_var = tk.StringVar(value="00")
        vcmd = (root.register(self.limit_size), '%P')

        # Create frames
        self.time_frame = tk.Frame(root, bg='#353535')
        self.time_frame.grid(row=0, column=0, sticky='nsew')
        self.button_frame = tk.Frame(root, bg='#353535')
        self.button_frame.grid(row=1, column=0, sticky='nsew')

        # Configure grid weights for resizing
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.time_frame.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.time_frame.rowconfigure(0, weight=1)
        self.button_frame.columnconfigure((0, 1), weight=1)
        self.button_frame.rowconfigure(0, weight=1)
        # Time entries and labels
        self.hours = ttk.Entry(self.time_frame, textvariable=self.hours_var, font=("Arial", 48), width=2, justify='center', validate='key', validatecommand=vcmd)
        self.hours.grid(row=0, column=0, sticky='nsew')
        self.hours.bind("<FocusIn>", self.clear_default)
        self.hours.bind("<FocusOut>", self.reset_if_empty)

        self.colon1 = tk.Label(self.time_frame, text=":", font=("Arial", 48), fg='white', bg='#353535')
        self.colon1.grid(row=0, column=1, sticky='nsew')

        self.minutes = ttk.Entry(self.time_frame, textvariable=self.minutes_var, font=("Arial", 48), width=2, justify='center', validate='key', validatecommand=vcmd)
        self.minutes.grid(row=0, column=2, sticky='nsew')
        self.minutes.bind("<FocusIn>", self.clear_default)
        self.minutes.bind("<FocusOut>", self.reset_if_empty)

        self.colon2 = tk.Label(self.time_frame, text=":", font=("Arial", 48), fg='white', bg='#353535')
        self.colon2.grid(row=0, column=3, sticky='nsew')

        self.seconds = ttk.Entry(self.time_frame, textvariable=self.seconds_var, font=("Arial", 48), width=2, justify='center', validate='key', validatecommand=vcmd)
        self.seconds.grid(row=0, column=4, sticky='nsew')
        self.seconds.bind("<FocusIn>", self.clear_default)
        self.seconds.bind("<FocusOut>", self.reset_if_empty)

        # Start and Reset buttons
        self.style.configure('Custom.TButton',
                     background='#353535',
                     foreground='white',
                     borderwidth=1,
                     relief='solid')
        #Alert Style
        self.style.configure('Dialog.TButton',
                             background='#353535',
                             foreground='white',
                             borderwidth=1,
                             relief='solid')
        self.style.map('Dialog.TButton',
                       background=[('active', '#454545')])
        self.start_button = ttk.Button(self.button_frame, text="Start", command=self.start_timer, style='Custom.TButton')
        self.start_button.grid(row=0, column=0, sticky='nsew')

        self.reset_button = ttk.Button(self.button_frame, text="Reset", command=self.reset_timer, style='Custom.TButton')
        self.reset_button.grid(row=0, column=1, sticky='nsew')

        self.sound = pygame.mixer.Sound(self.resource_path('sounds/end.wav'))
        self.time_in_seconds = 0
        self.running = False

    def resource_path(self, relative_path):
        try:
            base_path = sys._MEIPASS
        except AttributeError:
            base_path = os.path.dirname(__file__)  
        return os.path.join(base_path, relative_path)

    def show_notification(self):
        CustomDialog(self.root, title="ALERT", message="Time's up!")
        self.stop_sound() 

    def stop_sound(self, event=None):
        if self.sound_channel.get_busy():
            self.sound_channel.stop()

    def clear_default(self, event):
        entry = event.widget
        if entry.get() == "00":
            entry.delete(0, tk.END)

    def reset_if_empty(self, event):
        entry = event.widget
        if not entry.get():
            entry.insert(0, "00")

    def limit_size(self, P):
        return len(P) <= 2

    def update_timer(self):
        if self.running:
            if self.time_in_seconds > 0:
                self.time_in_seconds -= 1
                hours, remainder = divmod(self.time_in_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                self.time_label.config(text=f"{hours:02}:{minutes:02}:{seconds:02}")
                self.root.after(1000, self.update_timer)
            else:
                self.running = False
                self.sound_channel = pygame.mixer.Channel(0)
                self.sound_channel.play(self.sound, loops=-1)
                self.show_notification()
                self.time_label.grid_forget()
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
                    self.time_label = tk.Label(self.time_frame, text=f"{hours:02}:{minutes:02}:{seconds:02}", font=("Arial", 48), fg='white', bg='#353535')
                    self.time_label.grid(row=0, column=0, columnspan=5, sticky='nsew')
                    self.time_frame.columnconfigure(0, weight=1)
                    self.running = True
                    self.update_timer()
                else:
                    messagebox.showerror("Invalid Input", "Please enter a positive time.")
            except ValueError:
                messagebox.showerror("Invalid Input", "Please enter valid numbers in the fields.")

    def reset_timer(self):
        self.running = False
        self.time_in_seconds = 0
        self.hours.unbind("<FocusIn>")
        self.minutes.unbind("<FocusIn>")
        self.seconds.unbind("<FocusIn>")
        self.hours.unbind("<FocusOut>")
        self.minutes.unbind("<FocusOut>")
        self.seconds.unbind("<FocusOut>")
        self.hours_var.set("00")
        self.minutes_var.set("00")
        self.seconds_var.set("00")
        self.hours.bind("<FocusIn>", self.clear_default)
        self.minutes.bind("<FocusIn>", self.clear_default)
        self.seconds.bind("<FocusIn>", self.clear_default)
        self.hours.bind("<FocusOut>", self.reset_if_empty)
        self.minutes.bind("<FocusOut>", self.reset_if_empty)
        self.seconds.bind("<FocusOut>", self.reset_if_empty)
        if hasattr(self, 'time_label'):
            self.time_label.grid_forget()
            self.pack_time_entries()

    def pack_time_entries(self):
        self.hours.grid(row=0, column=0, sticky='nsew')
        self.colon1.grid(row=0, column=1, sticky='nsew')
        self.minutes.grid(row=0, column=2, sticky='nsew')
        self.colon2.grid(row=0, column=3, sticky='nsew')
        self.seconds.grid(row=0, column=4, sticky='nsew')
        # Reset column weights
        self.time_frame.columnconfigure((0, 2, 4), weight=1)
        self.time_frame.columnconfigure((1, 3), weight=0)

    def unpack_time_entries(self):
        self.hours.grid_forget()
        self.colon1.grid_forget()
        self.minutes.grid_forget()
        self.colon2.grid_forget()
        self.seconds.grid_forget()

class CustomDialog(tk.Toplevel):
    def __init__(self, parent, title=None, message="Time's up!"):
        super().__init__(parent)
        self.transient(parent)
        if title:
            self.title(title)
        self.configure(bg='#353535')  
        self.parent = parent
        self.result = None
        self.grab_set()
        body = tk.Frame(self, bg='#353535')
        self.body(body, message)
        body.pack(padx=20, pady=20)
        self.update_idletasks()
        x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (self.winfo_width() // 2)
        y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (self.winfo_height() // 2)
        self.geometry(f"+{x}+{y}")
        self.wait_window(self)

    def body(self, master, message):
        label = tk.Label(master, text=message, fg='white', bg='#353535', font=('Segoe UI', 12))
        label.pack()
        button = ttk.Button(master, text="OK", command=self.ok_pressed, style='Dialog.TButton')
        button.pack(pady=(20, 0))

    def ok_pressed(self):
        self.destroy()

if __name__ == "__main__":
    root = ThemedTk(theme="equilux")
    root.configure(bg='#353535')
    app = TimerApp(root)
    root.mainloop()

#Icon source 
#Clock by NicholasJudy456 - uploaded on October 13, 2016, 10:20 pm https://openclipart.org/detail/263940/clock#google_vignette
