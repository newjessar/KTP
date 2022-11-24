
import numpy as np

class Student:
    def __init__(self):
        self.studentName        = ""
        self.studentNumber      = int
        self.passedCourses      = []
        self.wishedCourses      = []
        self.passedElective     = int
        self.passedPractices    = int
        self.currentYear        = int
        self.currentBlock       = int
        self.motivation         = int
        self.orientation        = int
    
    def firstYear(self):
        if self.currentYear == 1:
            return True
        return False
    
    def passPracticals(self):
        if self.passedPractices >= 3:
            return True
        return False
            
    # Get orientation of the student
    def getOrientation(self):
        return self.orientation
    
    # Get the wished courses of the student
    def wishedCoursess(self):
        return self.wishedCourses

        
