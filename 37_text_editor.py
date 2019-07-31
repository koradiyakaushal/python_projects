import sys
# from Tkinter import *
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
text = tk.Text(root)
text.grid()


def save_as():
    global text
    t = text.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, "w+")
    file1.write(t)
    file1.close()


button = tk.Button(root, text="Save", command=save_as)
button.grid()


root.mainloop()

# https://www.instructables.com/id/Create-a-Simple-Python-Text-Editor/
