
import numpy as np
from courses import Courses
from student import Student
from course import Course
import knowledge_Base as Knowledge_Base
from academic_planning import Academic_planning

class Knowledge_Base():
    
    def __init__(self, student : Student):
        ## Domian Model
        self.courses = Courses()
        self.ap = Academic_planning()
        self.st = Student


        self.courses.initiateCourses()
        self.courses.getAllYears()
        
        self.courList = self.courses.getAllcourses()
        self.yearOneC = self.courses.yearOneCour
        self.yearTwoC = self.courses.yearTwoCour
        self.yearThreeC = self.courses.yearThreeCour
        self.achievement = int
        self.advise = False
        self.examCommittee = "Contact the exam Committee"
        
    ## Rule Model

    # rule 1 - table 1 - all years
    def practicalNoPreReq(self):
        for course in self.ap.possible_courses:
            if course.getPractical() and not course.getPre_requisite():
                course.pre_requisite_courses = course.advised_courses
                course.pre_requisite = True
                return

    # rule 2 - table 1 - all years
    def recommend5ECT1(self):
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 0:
            self.ap.recommended_Extra5ECTS = True
            return 

    #TODO: what average grade is enough
    # rule 3 - table 1 - all years
    def recommend5ECT(self):
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 1 and self.st.average_grade >= 7:
            self.ap.recommended_Extra5ECTS = True
            return 
    
    # rule 4 - table 1 - all years
    def recommend5ECT1(self):
        if not self.st.want5ECTS or not self.st.validReason() or self.st.failedCourses > 1:
            self.ap.recommended_Extra5ECTS = False
            return

            

    
    
    # def fourth_course(self):
    #     for wish in self.st.wishedCourses:
    #         if self.advis.courList[wish].getOrientation() == self.st.getOrientation() and self.st.motivation > 7:
    #             self.advise = True
                    
    # def above_four_course(self):
    #     for wish in self.st.wishedCourses:
    #         if self.adviscourList[wish].getOrientation() == self.st.getOrientation():
    #             if self.st.motivation > 9 :
    #                 self.advise = True       
        
    

## 1st Year Students

    















## 2nd+ Year Students
    

    # rule 13
    def 