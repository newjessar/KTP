from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk

class Frame_start_screen(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        
        self.frame = ttk.LabelFrame(self)
        self.frame.pack()
        
        button_frame = LabelFrame(self.frame)
        text_frame = LabelFrame(self.frame)
        
        button_frame.grid(row=0,column=0)
        text_frame.grid(row=1,column=0)
        
        start_button = Button(button_frame,text= "START",command=self.start_action)
        quit_button = Button(button_frame,text= "QUIT",command=self.quit_action)
        label = Label(text_frame,text="Press start to begin choosing a course")
        
        start_button.grid(row=0,column=0)
        quit_button.grid(row=0,column=1)
        label.grid(row=0,column=0)
        
    def start_action(self):
        global status
        status = "mandatory_courses"
        
    def quit_action(self):
        global status
        status = "quit"
        