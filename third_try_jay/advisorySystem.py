
import numpy as np
from courses import Courses
from student import Student
from course import Course
import rules as Rules

class Advisory():
    
    def __init__(self, student : Student):
        self.courses = Courses()
        self.st = student


        self.courses.initiateCourses()
        self.courses.getAllYears()
        
        self.courList = self.courses.getAllcourses()
        self.yearOneC = self.courses.yearOneCour
        self.yearTwoeC = self.courses.yearTwoCour
        self.yearThreeC = self.courses.yearThreeCour
        self.achievement = int
        self.advise = False
        self.examCommittee = "Contact the exam Committee"
        
        
        
    


    
