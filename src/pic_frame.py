import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

#creating gui
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("sun1.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Picture Frame")
root.geometry("500x500")
root.mainloop()

















