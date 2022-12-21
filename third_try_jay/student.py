
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
        self.propaedeuticPhasePassed = bool
        self.startedBachelorProject = bool
    
    def determinePropaedeuticPhasePassed(self):
        firstYearCourses = [course for course in self.passedCourses if course.year == 1]
        if len(firstYearCourses == 12):
            return True
        else:
            return False

    def calculateAverageGrade(self):
        return statistics.mean(self.passedCourses)

    def calculateCurrentECTS(self):
        total = 0
        for course in self.passedCourses:
            total += course.credit 
        return total

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
    
    # Get passed courses of the student
    def getPassedCourses(self):
        return self.passedCourses

    # Get orientation of the student
    def getOrientation(self):
        return self.orientation
    
    # Get the wished courses of the student
    def wishedCoursess(self):
        return self.wishedCourses

    
        
