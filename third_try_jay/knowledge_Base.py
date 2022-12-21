
import numpy as np
from courses import Courses
from student import Student
from course import Course
import knowledge_Base as Knowledge_Base

class Knowledge_Base():
    
    def __init__(self, student : Student):
        ## Domian Model
        self.courses = Courses()
        self.courses = Courses()
        self.st = Student


        self.courses.initiateCourses()
        self.courses.getAllYears()
        
        self.courList = self.courses.getAllcourses()
        self.yearOneC = self.courses.yearOneCour
        self.yearTwoeC = self.courses.yearTwoCour
        self.yearThreeC = self.courses.yearThreeCour
        self.achievement = int
        self.advise = False
        self.examCommittee = "Contact the exam Committee"
        
     ## Rule Model
    def practicalOrPrerequisites(self):
        for wish in self.st.wishedCourses:
            course = self.advis.courList[wish]
            if course.getPractical() == True:
                if course.pre_requisite() == True :
                    return course.getPractical()
                
                
    def extraFiveEC_Required(self):
        for wish in self.st.wishedCourses:
            course = self.advis.courList[wish]
            if course.getPractical() == True:
                if course.pre_requisite() == True :
                    return course.getPractical()
    
    
         
    def fourth_course(self):
        for wish in self.st.wishedCourses:
            if self.advis.courList[wish].getOrientation() == self.st.getOrientation():
                if self.st.motivation > 7 :
                    self.advise = True
                    
    def above_four_course(self):
        for wish in self.st.wishedCourses:
            if self.adviscourList[wish].getOrientation() == self.st.getOrientation():
                if self.st.motivation > 9 :
                    self.advise = True       
        
    


    
