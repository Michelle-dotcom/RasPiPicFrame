import os
from pathlib import Path
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

#getting pictures from folder
def get_pictures():
    pictures = []
    """default folder structure:
    project
        src
        pictures
        myenv
    """
    parent_folder = Path.cwd().parent
    print("p: ", parent_folder)
    pic_folder = Path(parent_folder/"pictures")
    print("pic: ", pic_folder)
    for file in os.listdir(pic_folder):
        pictures.append(str(file))
    return pictures

fld = str(Path(Path.cwd().parent/"pictures"))

#creating gui
root = tk.Tk()
root.title("Picture Frame")
root.geometry("500x500")

#pics = get_pictures()

#adding pics to gui
#for p in pics:
    
pic=Image.open(fld+"/"+"sun.jpg")
img = tk.PhotoImage(pic)
panel = tk.Label(root,image = img)
#label =tk.Label()
#label.photos = img
#label.pack()
panel.pack(side = "bottom", fill = "both", expand = "yes")
    
root.mainloop()

















