from tkinter import *
import GUI1
import GUI2

def call_GUI1():
    win1 = Toplevel(root)
    GUI1.GUI1(win1)
    return

def call_GUI2():
    win2 = Toplevel(root)
    GUI2.GUI2(win2)
    return

# the first gui owns the root window
if __name__ == "__main__":
    root = Tk()
    root.title('Caller GUI')
    root.minsize(720, 600)
    button_1 = Button(root, text='Call GUI1', width='20', height='20', command=call_GUI1)
    button_1.pack()
    button_2 = Button(root, text='Call GUI2', width='20', height='20', command=call_GUI2)
    button_2.pack()
    root.mainloop()






import tkinter as tk

def GUI1(Frame):
    label = tk.Label(Frame, text="Hello from %s" % __file__)
    label.pack(padx=20, pady=20)
    return

if __name__ == "__main__":
    root = tk.Tk()
    GUI1(root)
    root.mainloop()