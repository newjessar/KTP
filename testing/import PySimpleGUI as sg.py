import tkinter as tk
import tkinter.messagebox



def displaydate():
    win1 = tk.Tk()
    frA = tk.Frame()
    labA = tk.Label(master=frA, text="This is A Frame")
    labA.pack()
    frb = tk.Frame()
    labB = tk.Label(master=frb, text="This is B Frame")
    labB.pack()
    frb.pack()
    frA.pack()

    
root = tk.Tk()
root.title('Pop up MessageBox')
butn = tk.Button(root, text="Display Dat", padx=7, pady=7, width=12,command=displaydate)
butn.pack(pady=11)
root.geometry('400x400+400+350')
root.mainloop()

