# Gui trail
import numpy as np
from student import Student
from advisorySystem import Advisory
from gui import GuiAdv




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
    guiADV = GuiAdv(advisory)
    # advisory.Fourth_course()
    # print(advisory.courList[1].getTitle())
    # for item in range:
        
    

    guiADV.makeLayout()
    
    

if __name__ == "__main__":
    main()