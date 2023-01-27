
import statistics

class Student:
    def __init__(self):
        self.studentName        = ""
        self.studentNumber      = None
        self.passedCourses      = []
        self.want5ECTS          = None
        self.reason5ECTS        = None
        self.failedCourses      = None
        self.currentBlock       = None
        self.currentYear        = None
        self.orientation        = None
        self.averageGrade       = 8
        self.language           = True # True = English, False = Dutch 
        self.propaedeuticPhasePassed = None
        self.startedBachelorProject = False
    
    def determinePropaedeuticPhasePassed(self):
        firstYearCourses = [course for course in self.passedCourses if course.year == 1]
        if len(firstYearCourses) == 12:
            return True
        else:
            return False

    def calculateAverageGrade(self):
        return statistics.mean([course.grade for course in self.passedCourses]+[course.grade for course in self.failedCourses])

    def calculateCurrentECTS(self):
        total = 0
        for course in self.passedCourses:
            total += course.credit 
        return total

    def validReason(self):
        if self.reason5ECTS == "Bored" or self.reason5ECTS == "Applying honours":
            return True
        else:
            return False

    def notInPassed(self,name):
        for course in self.passedCourses:
            if course.title == name:
                return False
        return True

    def firstYear(self):
        if self.currentYear == 1:
            return True
        return False
    
    # Get passed courses of the student
    def getPassedCourses(self):
        return self.passedCourses

    # Get orientation of the student
    def getOrientation(self):
        return self.orientation

    
        
