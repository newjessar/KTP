
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

    # Rule 1 - table 1 - all years
    # This functiuon checks for if there are no pre-requisites for a courses 
    # then it adds the advised courses in pre-requisites
    def practicalNoPreReq(self):
        for course in self.ap.possible_courses:
            if course.getPractical() and not course.getPre_requisite():
                course.pre_requisite_courses = course.advised_courses
                course.pre_requisite = True
                return

    # rule 2 - table 1 - all years
    def recommend5ECTS1(self):
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 0:
            self.ap.recommended_Extra5ECTS = True
            return 

    #TODO: what average grade is enough
    # rule 3 - table 1 - all years
    def recommend5ECTS2(self):
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 1 and self.st.average_grade >= 7:
            self.ap.recommended_Extra5ECTS = True
            return 
    
    # rule 4 - table 1 - all years
    def notRecommend5ECTS(self):
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
    # rule 1 - set all mandatory first year courses as recomended and puit all mandatory second and third year courses as possible
    def year2mandatory(self):
        if self.ap.recommended_courses == [] and self.ap.possible_courses == []:
            year1,year2,year3 = self.courses.getMandatoryBlockCourses(self.ap.planBlock)
            for course in year1:
                self.ap.recommended_courses.append(course)
            for course in year2:
                self.ap.possible_courses.append(course)                
            for course in year3:
                self.ap.possible_courses.append(course)

            self.ap.checkedMandatoryCourses = True
        return

    # rule 2 - remove courses that have their prerequisites not met
    def deleteNotPossible(self):
        if self.ap.planYear == 1:
            return
        new_possible_courses = []
        for course in self.ap.possible_courses:
            if self.ap.preReqMet(course,self.st.passedCourses):
                new_possible_courses.append(course)
        self.ap.possible_courses = new_possible_courses
        return

    # rule 3 - add the course with the most prerequisites to recomended courses
    def transferHighestPreReq(self):
        if self.ap.planYear!= 1 and self.ap.possible_courses != [] and self.ap.creditsRecomendedCourses() <= 15 and not self.ap.checkedPracticalCourses:
            self.ap.recommended_courses.append(self.ap.highestPreReg())
            return

    # rule 4 - 



    # rule 10 - if the student's orientation is cs, move the non-cs courses from the possible courses to other available electives
    def moveNONCSCourses(self):
        if self.ap.checkedElectiveCourses == True and self.ap.planYear != 1 and self.st.getOrientation() == 2:
            for course in self.ap.possible_courses:
                if course.orientation == 1:
                    self.ap.other_available_electives.append(course)
            self.ap.finishedElectives = True
            return

    # rule 11 - if the student's orientation is non-cs, move the cs courses from the possible courses to other available electives
    def moveCSCourses(self):
        if self.ap.checkedElectiveCourses == True and self.ap.planYear != 1 and self.st.getOrientation() == 1:
            for course in self.ap.possible_courses:
                if course.orientation == 2:
                    self.ap.other_available_electives.append(course)
            self.ap.finishedElectives = True
            return

    # rule 12 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def presentAdvice1(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits >= 15 and self.ap.recommended_Extra5ECTS == False:
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = False
            self.ap.finished = True
            return


    # rule 13 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def presentAdvice2(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits() >= 20 and self.ap.recommended_Extra5ECTS == True:
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = False
            self.ap.finished = True
            return

    # rule 14 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def presentAdvice3(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits() <= 15 and self.ap.recommended_Extra5ECTS == False:
            self.ap.showOtherCourses = True
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = True
            self.ap.finished = True
            return

    # rule 15 - if the 
    def presentAdvice4(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits() <= 20 and self.ap.recommended_Extra5ECTS == True:
            self.ap.showOtherCourses = True
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = True
            self.ap.finished = True
            return
    
    # rule 16 - if the planning is for the first block of the third or higher year and requirements to start the Bachelor Project are met, recommend it  
    def addBachelorProjectAIn1A(self):
        passedCourses = self.st.getPassedCourses()
        if self.ap.planYear >= 3 and self.ap.planBlock == "1a" and self.st.calculateCurrentECTS >= 135 and \
        self.st.determinePropaedeuticPhasePassed == True and "Statistics" in passedCourses and \
        "Data Analytics and Communication" in passedCourses and self.ap.checkedMandatoryCourses == True and \
        self.ap.checkedPracticalCourses == True and self.st.startedBachelorProject == False:
            self.ap.recommended_courses.append("Bachelor Project A")
            return

    # rule 17 - if the planning is for the second block and the Bachelor Project is already started, recommend it  
    def addBachelorProjectBIn1B(self):
        if self.ap.planYear >= 3 and self.ap.planBlock == "1b" and self.ap.checkedMandatoryCourses == False and \
        self.ap.checkedPracticalCourses == False and self.st.startedBachelorProject == True:
            self.ap.recommended_courses.append("Bachelor Project B")
            return
    

    # rule 18 - if the planning is for the third block and requirements to start the Bachelor Project are met, recommend it  
    def addBachelorProjectAIn2A(self):
        passedCourses = self.st.getPassedCourses()
        if self.ap.planBlock == "2a" and self.st.calculateCurrentECTS >= 135 and \
        self.st.determinePropaedeuticPhasePassed == True and "Statistics" in passedCourses and \
        "Data Analytics and Communication" in passedCourses and self.ap.checkedMandatoryCourses == True and \
        self.ap.checkedPracticalCourses == True and self.st.startedBachelorProject == False:
            self.ap.recommended_courses.append("Bachelor Project A")
            return

    # rule 19 - if the planning is for the fourth block and the Bachelor Project is already started, recommend it  
    def addBachelorProjectBIn2B(self):
        if self.ap.planYear >= 3 and self.ap.planBlock == "2b" and self.ap.checkedMandatoryCourses == False and \
        self.ap.checkedPracticalCourses == False and self.st.startedBachelorProject == True:
            self.ap.recommended_courses.append("Bachelor Project B")
            return