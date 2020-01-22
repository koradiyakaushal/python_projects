from tkinter import *
from googletrans import Translator
from tkinter.messagebox import showinfo

window = Tk()
window.title("Tanslator")
window.geometry("200x80")

translator = Translator()

def translate():
    word = entry.get()
    result = translator.translate(word, dest="en").text
    showinfo("Translation: ", result)

label = Label(window, text="Enter your word to translate: ")
label.grid(row=0, column=0)

entry = Entry(window)
entry.grid(row=1, column=0)

button = Button(window, text="Translate", command=translate)
button.grid(row=2, column=0, padx=10)

window.mainloop()