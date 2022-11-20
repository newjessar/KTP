from frame_root import Frame_root
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
from frame_start_screen import Frame_start_screen
from frame_passed_courses_mandatory import Frame_passed_courses_mandatory

class MainFrame(ttk.Frame):
    def __init__(self,container):
        super().__init__(container)
        global status 
        status = "start"
        
        root = Frame_root()
        
        if status=="start":
            root = Frame_start_screen(root)
        elif status=="mandatory_courses":
            root = Frame_passed_courses_mandatory(root)
        elif status=="quit":
            root.destroy()
                
        root.mainloop()


    
if __name__ == "__main__":
    root = Frame_root()
    frame = MainFrame(root)
    root.mainloop()