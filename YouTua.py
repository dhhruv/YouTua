import youtube_dl
import os
import os.path
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import shutil
import threading
import time
stop_thread = False

class MainWindow:

    THIS_FOLDER_G = ""
    if getattr(sys, "frozen", False):
        THIS_FOLDER_G = os.path.dirname(sys.executable)
    else:
        THIS_FOLDER_G = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, root):
        self.root = root
        self._url = tk.StringVar()
        self._savefolder = tk.StringVar()
        self._savefolder.set(os.getcwd())
        self._status = tk.StringVar()
        self._status.set("---")

        root.title("YouTua")
        root.configure(bg="#eeeeee")

        self.menu_bar = tk.Menu(
            root,
            bg="#eeeeee",
            relief=tk.FLAT
        )
        self.menu_bar.add_command(
            label="Help!",
            command=self.show_help_callback
        )
        self.menu_bar.add_command(
            label="About",
            command=self.show_about
        )

        root.configure(
            menu=self.menu_bar
        )

        self.folder_entry_label = tk.Label(
            root,
            text="Enter the Output Directory:",
            bg="#eeeeee",
            anchor=tk.W
        )
        self.folder_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=0,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.file_entry = tk.Entry(
            root,
            textvariable=self._savefolder,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.file_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=1,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.select_btn = tk.Button(
            root,
            text="SELECT OUTPUT FOLDER",
            command=self.select_folder_callback,
            width=42,
            bg="#1089ff",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.select_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=2,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.url_entry_label = tk.Label(
            root,
            text="Enter the URL (Link):",
            bg="#eeeeee",
            anchor=tk.W
        )
        self.url_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=3,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.url_entry = tk.Entry(
            root,
            textvariable=self._url,
            bg="#fff",
            exportselection=0,
            relief=tk.FLAT
        )
        self.url_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=4,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.download_btn = tk.Button(
            root,
            text="START DOWNLOAD",
            command=self.download_callback,
            bg="#1089ff",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.download_btn.grid(
            padx=(15, 6),
            pady=8,
            ipadx=24,
            ipady=6,
            row=5,
            column=0,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.stop_btn = tk.Button(
            root,
            text="STOP",
            command=self.stop_callback,
            bg="#1089ff",
            fg="#ffffff",
            bd=2,
            relief=tk.FLAT
        )
        self.stop_btn.grid(
            padx=(6, 15),
            pady=8,
            ipadx=24,
            ipady=6,
            row=5,
            column=2,
            columnspan=2,
            sticky=tk.W+tk.E+tk.N+tk.S
        )

        self.status_label = tk.Label(
            root,
            textvariable=self._status,
            bg="#eeeeee",
            anchor=tk.W,
            justify=tk.LEFT,
            relief=tk.FLAT,
            wraplength=350
        )
        self.status_label.grid(
            padx=12,
            pady=(0, 12),
            ipadx=0,
            ipady=1,
            row=7,
            column=0,
            columnspan=4,
            sticky=tk.W+tk.E+tk.N+tk.S
        )


    def select_folder_callback(self):
    	try:
    		name=filedialog.askdirectory()
    		self._savefolder.set(name)
    	except Exception as e:
    		self._status.set(e)
    		self.status_label.update()


    def download_callback(self):
    	global stop_thread
    	t1=threading.Thread(target=self.download)
    	t1.start()


    def download(self):
        try:
            with youtube_dl.YoutubeDL({'include_ads': False, 'outtmpl': self._savefolder.get()+"/%(title)s.%(ext)s", 'format': 'best', 'writeautomaticsub': True}) as ydl:
                global stop_thread
                self._status.set("Download Started..")
                self.status_label.update()
                while True:
                    global stop_thread
                    if stop_thread:
                        break
                    ydl.download([self._url.get()])
                    stop_thread = True
                self._status.set("Download Completed!!")
                self.status_label.update()
                messagebox.showinfo("YouTua","Download Completed!!")
        except Exception as e:
            self._status.set("URL Error: Please check the entered URL and try again..")
            self.status_label.update()
            messagebox.showinfo("YouTua","URL Error: Please check the entered URL and try again..")

    def stop_callback(self):
    	global stop_thread
    	stop_thread = True

    def show_help_callback(self):
        messagebox.showinfo(
            "Help!",
            """To be written..."""
        )

    def show_about(self):
        messagebox.showinfo("YouTua v1.0.0",
            """YouTua is a Program to download videos from YouTube.com and a few more sites in the best quality available..
Created and Managed by Dhruv Panchal.
https://github.com/dhhruv
            """)

ROOT = tk.Tk()
ROOT.resizable(height = False, width = False)
MAIN_WINDOW = MainWindow(ROOT)
ROOT.mainloop()