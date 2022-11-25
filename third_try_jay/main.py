# Gui trail
import numpy as np
from student import Student
from advisorySystem import Advisory
from gui import App
import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"



def main():
    student = Student()
    
    student.studentName     = "Jay Kay"
    student.studentNumber   = 302
    student.passedCourses   = [1, 3]
    student.wishedCourses   = [6]
    student.passedElective  = 0
    student.passedPractices = 0
    student.currentYear     = 2
    student.currentBlock    = 2
    student.motivation      = 7
    student.orientation     = 2
    
    advisory = Advisory(student)
    app = App(advisory)
    app.mainloop()

if __name__ == "__main__":
    main()