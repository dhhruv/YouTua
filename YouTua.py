#!/usr/bin/python
# -*- coding: utf-8 -*-

from youtuatools.YoutubeDL import YoutubeDL
import os
import os.path
import sys
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import *
import shutil
import threading
from pathlib import Path


class MainWindow:

    THIS_FOLDER_G = ''
    if getattr(sys, 'frozen', False):
        THIS_FOLDER_G = os.path.dirname(sys.executable)
    else:
        THIS_FOLDER_G = os.path.dirname(os.path.realpath(__file__))

    def __init__(self, root):
        self.root = root
        self._url = tk.StringVar()
        self._savefolder = tk.StringVar()
        self._savefolder.set(os.getcwd())
        self._status = tk.StringVar()
        self.advs = tk.BooleanVar()
        self._subtitles = tk.BooleanVar()
        self._subtitles.set(False)
        self.vid_format = tk.StringVar()
        self.vid_format.set('select')
        self._status.set('---')
        self.stopFlag = False

        root.title('YouTua')
        root.configure(bg='#eeeeee')

        try:
            icon_img = tk.Image('photo', file=self.THIS_FOLDER_G
                                + './files/YouTua.ico')
            root.call('wm', 'iconphoto', root._w, icon_img)
        except Exception:
            pass

        self.menu_bar = tk.Menu(root, bg='#eeeeee', relief=tk.FLAT)
        self.menu_bar.add_command(label='Help!',
                                  command=self.show_help_callback)
        self.menu_bar.add_command(label='About',
                                  command=self.show_about)

        root.configure(menu=self.menu_bar)

        self.folder_entry_label = tk.Label(root,
                text='Enter the Output Directory:', bg='#eeeeee',
                anchor=tk.W)
        self.folder_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=0,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.file_entry = tk.Entry(root, textvariable=self._savefolder,
                                   bg='#fff', exportselection=0,
                                   relief=tk.FLAT)
        self.file_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=1,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.select_btn = tk.Button(
            root,
            text='SELECT OUTPUT FOLDER',
            command=self.select_folder_callback,
            width=42,
            bg='#3498db',
            fg='#ffffff',
            bd=2,
            relief=tk.FLAT,
            )
        self.select_btn.grid(
            padx=15,
            pady=8,
            ipadx=24,
            ipady=6,
            row=2,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.url_entry_label = tk.Label(root,
                text='Enter the URL (Link):', bg='#eeeeee', anchor=tk.W)
        self.url_entry_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=3,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.url_entry = tk.Entry(root, textvariable=self._url,
                                  bg='#fff', exportselection=0,
                                  relief=tk.FLAT)
        self.url_entry.grid(
            padx=15,
            pady=6,
            ipadx=8,
            ipady=8,
            row=4,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.adv_button = tk.Checkbutton(
            root,
            text='Maximum Resolution Settings:',
            variable=self.advs,
            onvalue=True,
            offvalue=False,
            command=self.check_settings,
            bg='#eeeeee',
            anchor=tk.W,
            )

        self.adv_button.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=5,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.format_label = tk.Label(root, text='Format:', bg='#eeeeee'
                , state='disabled', anchor=tk.W)
        self.format_label.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=6,
            column=0,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.mp4_button = tk.Radiobutton(
            root,
            text='mp4',
            variable=self.vid_format,
            value='mp4',
            bg='#eeeeee',
            state='disabled',
            anchor=tk.W,
            )

        self.mp4_button.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=6,
            column=2,
            columnspan=1,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.mkv_button = tk.Radiobutton(
            root,
            text='mkv',
            variable=self.vid_format,
            value='mkv',
            bg='#eeeeee',
            state='disabled',
            anchor=tk.W,
            )

        self.mkv_button.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=6,
            column=3,
            columnspan=1,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.subtitles_button = tk.Checkbutton(
            root,
            text='Subtitles (If available):',
            variable=self._subtitles,
            onvalue=True,
            offvalue=False,
            bg='#eeeeee',
            anchor=tk.W,
            )

        self.subtitles_button.grid(
            padx=12,
            pady=(8, 0),
            ipadx=0,
            ipady=1,
            row=7,
            column=0,
            columnspan=2,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.download_btn = tk.Button(
            root,
            text='START DOWNLOAD (MAX RES<=720p)',
            command=self.download_callback,
            bg='#27ae60',
            fg='#ffffff',
            bd=2,
            relief=tk.FLAT,
            )
        self.download_btn.grid(
            padx=(15, 6),
            pady=8,
            ipadx=24,
            ipady=6,
            row=8,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

        self.status_label = tk.Label(
            root,
            textvariable=self._status,
            bg='#eeeeee',
            anchor=tk.W,
            justify=tk.LEFT,
            relief=tk.FLAT,
            wraplength=350,
            )
        self.status_label.grid(
            padx=12,
            pady=(0, 12),
            ipadx=0,
            ipady=1,
            row=9,
            column=0,
            columnspan=4,
            sticky=tk.W + tk.E + tk.N + tk.S,
            )

    def check_settings(self):
        if self.advs.get():
            self.vid_format.set('mp4')
            self.format_label['state'] = 'normal'
            self.mp4_button['state'] = 'normal'
            self.mkv_button['state'] = 'normal'
            self.download_btn['text'] = \
                'START DOWNLOAD (MAX RES<=2160p)'
        else:
            self.format_label['state'] = 'disabled'
            self.mp4_button['state'] = 'disabled'
            self.mkv_button['state'] = 'disabled'
            self.vid_format.set('select')
            self.download_btn['text'] = 'START DOWNLOAD (MAX RES<=720p)'

    def select_folder_callback(self):
        try:
            name = filedialog.askdirectory()
            self._savefolder.set(name)
        except Exception as e:
            self._status.set(e)
            self.status_label.update()

    def download_callback(self):
        newPath = Path(self._savefolder.get())
        if newPath.is_dir():
            pass
        else:
            messagebox.showinfo('YouTua',
                                'Please Enter a valid Folder URL !!')
            return
        if len(self._url.get()) == 0:
            messagebox.showinfo('YouTua',
                                'Please Enter a valid URL to download !!'
                                )
            return
        t1 = threading.Thread(target=self.download, daemon=True)
        t1.start()

    def download(self):
        try:
            if str(self.vid_format.get()) == 'mp4':
                with YoutubeDL({
                    'include_ads': False,
                    'outtmpl': self._savefolder.get()
                        + '/%(title)s.%(ext)s',
                    'format': 'bestvideo[ext!=webm]‌​+bestaudio[ext!=webm]‌​/best[ext!=webm]',
                    'writeautomaticsub': self._subtitles.get(),
                    'ffmpeg_location': ffmpeg_location,
                    }) as ydl:
                    self._status.set('Download Started..')
                    self.status_label.update()
                    ydl.download([self._url.get()])
                    self._status.set('Download Completed!!')
                    self.status_label.update()
                    messagebox.showinfo('YouTua', 'Download Completed!!'
                            )
            elif str(self.vid_format.get()) == 'mkv':
                with YoutubeDL({
                    'include_ads': False,
                    'outtmpl': self._savefolder.get()
                        + '/%(title)s.%(ext)s',
                    'format': 'bestvideo+bestaudio/best',
                    'writeautomaticsub': self._subtitles.get(),
                    'ffmpeg_location': ffmpeg_location,
                    }) as ydl:
                    self._status.set('Download Started..')
                    self.status_label.update()
                    ydl.download([self._url.get()])
                    self._status.set('Download Completed!!')
                    self.status_label.update()
                    messagebox.showinfo('YouTua', 'Download Completed!!'
                            )
            else:
                with YoutubeDL({
                    'include_ads': False,
                    'outtmpl': self._savefolder.get()
                        + '/%(title)s.%(ext)s',
                    'format': 'best',
                    'writeautomaticsub': self._subtitles.get(),
                    }) as ydl:
                    self._status.set('Download Started..')
                    self.status_label.update()
                    ydl.download([self._url.get()])
                    self._status.set('Download Completed!!')
                    self.status_label.update()
                    messagebox.showinfo('YouTua', 'Download Completed!!'
                            )
        except Exception as e:
            self._status.set('URL Error: Please check the entered URL and try again !!'
                             )
            self.status_label.update()
            messagebox.showinfo('YouTua',
                                'URL Error: Please check the entered URL and try again !!'
                                )

    def show_help_callback(self):
        messagebox.showinfo('Help!',
                            """1. Select the OUTPUT Folder by manually adding path or selecting the FOLDER using the SELECT FOLDER Button.
(By Default the OUTPUT FOLDER is set to the current directory.)
2. Enter the Link of Youtube Video you want to download.
3. For Downloading video with RESOLUTION<=720p proceed normally to download.
4. For Downloading video with MAXIMUM RESOLUTION (=>720p) available according the video link, check the MAX RES Settings and choose the output format (.mp4 or .mkv) as per preferences. 
5. To download the available subtitles check the subtitles button.
6. Click START DOWNLOAD and enjoy.
Note:- This is a Pre-release so STOP Button is under implementation.
P.S. Wait until the video is downloaded.""")

    def show_about(self):
        messagebox.showinfo('YouTua v1.3.0',
                            """YouTua is a Program to download videos/playlists from YouTube.com and a few more sites in the best quality available..
It is released to the public domain, which means you can modify it, redistribute it or use it however you like.
Managed by Dhruv Panchal.
https://github.com/dhhruv
            """)


ROOT = tk.Tk()
bundle_dir = getattr(sys, '_MEIPASS',
                     os.path.abspath(os.path.dirname(__file__)))
path_to_ico = os.path.abspath(os.path.join(bundle_dir, 'YouTua.ico'))
bundle_dir2 = getattr(sys, '_MEIPASS',
                      os.path.abspath(os.path.dirname(__file__)))
ffmpeg_location = os.path.abspath(os.path.join(bundle_dir2, 'ffmpeg.exe'
                                  ))
ROOT.iconbitmap(path_to_ico)
ROOT.resizable(height=False, width=False)
MAIN_WINDOW = MainWindow(ROOT)
ROOT.mainloop()
