
import numpy as np
from courses import Courses
from student import Student
from course import Course
from advisorySystem import Advisory


class Knowledge_Base(object):
    
    def __init__(self):
        self.courses = Courses()
        self.st = Student
        self.advis = Advisory()
    
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

    ## Year
    
