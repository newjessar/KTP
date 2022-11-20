from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import ttk

class Frame_passed_courses_mandatory(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        
        self.frame = LabelFrame(self)
        self.frame.pack()
        
        button_frame = LabelFrame(self.frame)
        text_frame = LabelFrame(self.frame)
        
        button_frame.grid(row=0,column=0)
        text_frame.grid(row=1,column=0)
        
        reset_button = Button(button_frame,text= "Reset",command=self.reset_action)
        quit_button = Button(button_frame,text= "Quit",command=self.quit_action)
        label = Label(text_frame,text="Select Mandatory Courses Passed")
        
        reset_button.grid(row=0,column=0)
        quit_button.grid(row=0,column=1)
        label.grid(row=0,column=0)
        
        select_frame = LabelFrame(text_frame)
        select_frame.grid(row=1,column=0)
        
        year1_frame = LabelFrame(select_frame)
        year2_frame = LabelFrame(select_frame)
        year3_frame = LabelFrame(select_frame)
        
        year1_frame.grid(row=0,column=0)
        year1_label = Label(year1_frame,text="year 1")
        year1_label.grid(row=0,column=0)
        
        year2_frame.grid(row=0,column=1)
        year2_label = Label(year2_frame,text="year 2")
        year2_label.grid(row=0,column=0)    
    
        year3_frame.grid(row=0,column=2)
        year3_label = Label(year3_frame,text="year 3")
        year3_label.grid(row=0,column=0)
        
        coursesYr1 = ["introduction to AI", "basic scientific skills", "cognitive psychology","linear algebra and multivariable calculus"]
        coursesYr2 = ["language and speech technology","statistics (for AI)","knowledge and agent technology"]
        coursesYr3 = ["Artificial intelligence 2"]
        coursesAll = [coursesYr1,coursesYr2,coursesYr3]
        courseVar = {}
        for year in coursesAll:
            for block in year:
                courseVar[block] = StringVar()
                
    def reset_action(self):
        global status
        status = "start"
    
    def quit_action(self):
        global status
        status = "quit"
        
        
                
        
        