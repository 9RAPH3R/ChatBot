import speech_recognition as sr
from tkinter import *
from tkinter import ttk

from tkinter import *
import tkinter as tk
try:
    import ttk as ttk
    import ScrolledText
except ImportError:
    import tkinter.ttk as ttk
    import tkinter.scrolledtext as ScrolledText


r = sr.Recognizer() 

root = tk.Tk() 
root.title('Test 1')

style = ttk.Style() 
style.theme_use('winnative')

photo = PhotoImage(file='microphone.png').subsample(20,20)

label1 = ttk.Label(root,text='User:')
label1.grid(row=0, column=0)

entry1 = ttk.Entry(root, width=30)
entry1.grid(row=0, column=1, columnspan=4)

def voice_click():
    
    with sr.Microphone() as source:
        print("Say Something:")
        audio = r.listen(source)
       
    try:
        message = r.recognize_google(audio)
        print("You said: " + message)
        entry1.focus()
        entry1.delete(0,END)
        entry1.insert(0,message)

    except Exception as e:
        print(e)

"To set the buttons and text widget"

MyButton1 = ttk.Button(root, text='Get Response',width=30)
MyButton1.grid(row=0, column=5)

MyButton2 = Button(root, image=photo, command=voice_click, bd=0, activebackground='#c1bfbf', overrelief='groove', relief='sunken')
MyButton2.grid(row=0, column=6)  

root.mainloop()


