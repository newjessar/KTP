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

 

def main():
    student = Student()
    
    student.studentName      = "Jay Kay"
    #student.studentNumber    = 302
    passedString = ["Imperative Programming (for AI)", "Introduction to Artificial Intelligence", \
        "Autonomous Systems", "Introduction to Logic (AI)", "General Linguistics", "Calculus for Artificial Intelligence", \
        "Basic Scientific Skills", "Linear Algebra and Multivariable Calculus", "Algorithms and Data Structures (AI)", "Cognitive Psychology", \
        "Statistics","Architectures of Intelligence", "Artificial Intelligence 1",\
        "Introduction to the Brain", "Language and Speech Technology","Data Analytics and Communication",\
            "Knowledge and Agent Technology", "Signals and Systems (for AI)"\
        ]
    print(len(passedString))
    courses = Courses()
    courses.initiateCourses()
    courses.getAllYears()
    courList = courses.getAllcourses()
    student.passedCourses = []
    for i in courList:
        if i.title in passedString:
            student.passedCourses.append(i)
    for course in student.passedCourses:
        if course.title == "Language and Speech Technology":
            course.grade = 10
        elif course.orientation == 1:
            course.grade = 9
        else:
            course.grade = 8

    student.currentYear      = 1
    student.currentBlock   = 3
    student.failedCourses    = 0
    student.language = True
    student.reason5ECTS = "bored"
    student.want5ECTS = True
    #student.motivation       = 7
    student.orientation      = None
    knowledge_Base = Knowledge_Base(student)
    # for course in knowledge_Base.courses:
    #     if course in student.passedCourses:
    #         course.grade=8
    knowledge_Base.doInference()
    print("recomended courses:")
    for i in knowledge_Base.ap.recommended_courses:
        print(i.title)

    print("\nrecomended electives:")
    for i in knowledge_Base.ap.recommended_electives:
        print(i.title)
    if knowledge_Base.ap.showOtherCourses:  
        print("\nother electives:")
        for i in knowledge_Base.ap.other_available_electives:
            print(i.title)
    
    #app = App(knowledge_Base)
    #app.mainloop()

if __name__ == "__main__":
    main()
