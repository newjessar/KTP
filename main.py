# Gui trail
import numpy as np
from student import Student
from knowledge_Base import Knowledge_Base
from gui import App
import tkinter.messagebox
import customtkinter
from courses import Courses

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

 
# Run the main.py file to start the program
def main():
    
    student = Student()
    knowledge_Base = Knowledge_Base(student)
    app = App(knowledge_Base)
    app.mainloop()

if __name__ == "__main__":
    main()
