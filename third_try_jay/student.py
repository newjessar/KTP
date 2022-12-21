
import statistics

class Student:
    def __init__(self):
        self.studentName        = ""
        self.studentNumber      = int
        self.passedCourses      = []
        self.advisedCourses     = []
        self.want5ECTS          = bool
        self.reason5ECTS        = str
        self.failedCourses      = int
        self.averageGrade       = int
        self.passedElective     = int
        self.passedPracticals   = int
        self.currentYear        = int
        self.currentBlock       = int
        self.motivation         = int
        self.orientation        = int
        self.dutchSpeaker       = False
    

    def calculateAverageGrade(self):
        return statistics.mean(self.passedCourses)

    def validReason(self):
        if self.reason5ECTS == "bored" or self.reason5ECTS == "applying honours":
            return True
        else:
            return False

    def firstYear(self):
        if self.currentYear == 1:
            return True
        return False
    
    def passPracticals(self):
        if self.passedPracticals >= 3:
            return True
        return False
            
    # Get orientation of the student
    def getOrientation(self):
        return self.orientation
    
    # Get the wished courses of the student
    def wishedCoursess(self):
        return self.wishedCourses

    
        
