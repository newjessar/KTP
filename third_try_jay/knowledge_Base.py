
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
        self.st = student
        self.ap.planYear = self.st.currentYear
        self.ap.planBlock = self.st.currentBlock

        self.courses.initiateCourses()
        for course in self.courses.allcourses:
            if course in self.st.passedCourses:
                course.grade=8

        self.courses.getAllYears()
        
        self.courList = self.courses.getAllcourses()
        self.yearOneC = self.courses.yearOneCour
        self.yearTwoC = self.courses.yearTwoCour
        self.yearThreeC = self.courses.yearThreeCour
        self.achievement = int
        #self.advise = False
        self.examCommittee = "Contact the exam Committee"
        
    ## Rule Model

    # Rule 1 - table 1 - all years
    # This functiuon checks for if there are no pre-requisites for a courses 
    # then it adds the advised courses in pre-requisites
    def allrule1_practicalNoPreReq(self):
        infer = False
        for course in self.ap.possible_courses:
            if course.getPractical() and not course.getPre_requisite():
                course.pre_requisite_courses = course.advised_courses
                course.pre_requisite = True
                infer = True
        return infer

    # rule 2 - table 1 - all years
    def allrule2_recommend5ECTS1(self):
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 0 and self.ap.recommended_Extra5ECTS == None:
            self.ap.recommended_Extra5ECTS = True
            return True
        else:
            return False

    #TODO: what average grade is enough
    # rule 3 - table 1 - all years
    def allrule3_recommend5ECTS2(self):
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 1 and self.st.average_grade >= 7 and self.ap.recommended_Extra5ECTS != None:
            self.ap.recommended_Extra5ECTS = True
            return True
        else:
            return False
    
    # rule 4 - table 1 - all years
    def allrule4_notRecommend5ECTS(self):
        if (not self.st.want5ECTS or not self.st.validReason() or self.st.failedCourses > 1) and self.ap.recommended_Extra5ECTS == None:
            self.ap.recommended_Extra5ECTS = False
            return True
        else:
            return False

    # rule 5 - table 1 - all years
    def allrule5_recommend5ECTSAndFinish(self):
        if self.st.want5ECTS and self.ap.creditsRecomendedCourses() == 20:
            self.ap.finished = True
            return True
        else:
            return False

    # rule 6 - table 1 - all years
    def allrule6_notRecommend5ECTSAndFinish(self):
        if not self.st.want5ECTS and self.ap.creditsRecomendedCourses() == 15:
            self.ap.finished = True
            return True
        else:
            return False

    # rule 7 - table 1 - all years
    def allrule7_passed3Practicals(self):
        if self.st.passPracticals >= 3:
            for course in self.courses:
                if course.practical == True:
                    course.practical = False
                    course.elective = True
            return True
        else:
            return False

    def allrule8(self):
        if self.st.orientation == None:
            orientation1 = []
            orientation2 = []
            for course in self.ap.possible_courses:
                if course.orientation == 1:
                    orientation1.append(course.grade)
                else: 
                    orientation2.append(course.grade)
            orientation1 = self.ap.averageGrade(orientation1)
            orientation2 = self.ap.averageGrade(orientation2)
            if orientation2 > orientation1:
                self.st.orientation = 2
            else:
                self.st.orientation = 1
            return True
        else:
            return False


# ============ 1st Year Students ============

# Rule 1 - set self.dvice to true if self.ap.planYear is true and recomended coursses is not empty and recomendedExtra5ECTS is false
    def year1rule1_isAdvised(self):
        return False
    #     if self.ap.planYear == 1 and self.ap.recommended_courses != [] and not self.ap.recommended_Extra5ECTS:
    #         self.ap.finished = True
    #         return True
    #     else:
    #         return False
        
 #  Rule 2 - if self.ap.planYear is 1 and recomended courses is empty, itterate through 
 # self.yearOne and add mendatory courses with self.block same as planBlock
 # recommend courses set from Ocasys (15 credits mandatory courses)
    def year1rule2_MandatoryRecomendation(self):
        infer = False
        if self.ap.planYear == 1 and self.ap.recommended_courses == []:
            for course in self.yearOneC:
                if course.mandatory and course.block == self.ap.planBlock:
                    self.ap.recommended_courses.append(course)
                    infer = True
        return infer
                
 # Rule 3 - if self.ap.planYear is 1 and RecommendExtra5Credits is true and planBlock is not 1, check the possible_courses and the courses with the highest pre-requisites value then add the 3 highest courses to the ap.recommended_courses
    def year1rule3_highestPossiblePreRequisites(self):
        infer = False
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and self.ap.planBlock != 1 and self.ap.possible_courses == [] and self.ap.finished != True:
            for course in self.courses.allcourses:
                if course.block == self.ap.planBlock and course.year != 1 and (all(x in self.st.passedCourses for x in course.pre_requisite_courses)):
                    self.ap.possible_courses.append(course)
                    infer = True
        return infer
        
 # Rule 4 - if self.ap.planYear is 1 and self.ap.recommended_Extra5ECTS is true: 
    # then itterate through the courses in possible_courses to calculate the averageGrade of the courses with orientation: 1 
    # delete the courses with orientation 2 from the possible_courses if they are lower than the avrage of the courses with orientation 1
    def year1rule4_deleteNonCSCoursesWithLowGrades(self):
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and not self.ap.checkedOrientation and self.st.orientation == 2:
            for course in self.ap.possible_courses:
                if course.orientation == 1:
                    self.ap.possible_courses.remove(course)
            self.ap.checkedOrientation = True
            return True
        else:
            return False


# Rule 5 - if self.ap.planYear is 1 and self.ap.recommended_Extra5ECTS is true:     
   # Academic Planning year: recommendExtra5Credits is set to true &1st year & (averagegrade for cs courses < non cs courses)
   # Delete cs courses from possible courses.
    def year1rule5_deleteCSCoursesWithLowGrades(self):
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and not self.ap.checkedOrientation and self.st.orientation == 1:
            for course in self.ap.possible_courses:
                if course.orientation == 2:
                    self.ap.possible_courses.remove(course)
            print([t.title for t in self.ap.possible_courses])
            print(self.ap.creditsPossibleCourses())
            self.ap.checkedOrientation = True
            return True
        else:
            return False
   
        
# Rule 6 - Check if there are mandatory courses in (Academic planning possible courses) & and if self.ap.planYear is 1
#  iterate through the possible courses and deelete the courses that are not mandatory
    def year1rule6_deleteNotMandatory(self):
        infer = False
        mandatoryCourse = 0
        if self.ap.planYear == 1:
            for course in self.ap.possible_courses:
                if course.mandatory:
                    mandatoryCourse = 1
            if mandatoryCourse == 1:
                self.ap.possible_courses = [y for y in self.ap.possible_courses if not y.mandatory]
                infer = True
        return infer

  
# Rule 7 - not course.mandatory in (Academic planning possible courses) & and if self.ap.planYear is 1 and if the student speaks Dutch
# itterate through the possible courses and check if the course language is false.
# if the course language is false, add the course to the recommended courses
    def year1rule7_addDutchCourses(self): 
        infer = False
        if self.ap.planYear == 1 and self.st.language == False and self.ap.checkedLanguages == None and self.ap.possible_courses != []:
            for course in self.ap.possible_courses:
                if not course.mandatory and course.language == False:
                    self.ap.recommended_courses.append(course)
                    infer = True
                    self.ap.checkedLanguages = True
        return infer
        
        
# Rule 8 - if there are no mandatory courses in (Academic planning possible courses) & does not speak Dutch
    def year1rule8_addEnglishCourses(self): 
        infer = False
        if self.ap.planYear == 1 and self.st.language == True and self.ap.checkedLanguages == None and self.ap.possible_courses != []:
            for course in self.ap.possible_courses:
                if not course.mandatory and course.language == True:
                    self.ap.recommended_courses.append(course)
                    infer = True
                    self.ap.checkedLanguages = True
        return infer        
        
        
        
# Rule 9 - if self.ap.planYear is 1 and student want5ECTS is true and recommend 5 extra credits is true:
# make recommend 5 extra credits true
    def year1rule9_addExtra5ECTS(self):
        infer = False
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and self.ap.creditsPossibleCourses() == 5:
            self.ap.recommended_courses.append(self.ap.possible_courses[0])
            self.ap.possible_courses = []
            self.ap.finished = True
            infer = True
        return infer
         

## 2nd+ Year Students
    # rule 1 - set all mandatory first year courses as recomended and puit all mandatory second and third year courses as possible
    def year2hrule1_year2mandatory(self):
        if self.ap.recommended_courses == [] and self.ap.possible_courses == []:
            year1,year2,year3 = self.courses.getMandatoryBlockCourses(self.ap.planBlock)
            for course in year1:
                self.ap.recommended_courses.append(course)
            for course in year2:
                self.ap.possible_courses.append(course)                
            for course in year3:
                self.ap.possible_courses.append(course)
            self.ap.checkedMandatoryCourses = True
            return True
        else:
            return False

    # rule 2 - remove courses that have their prerequisites not met
    def year2hrule2_deleteNotPossible(self):
        if self.ap.planYear == 1:
            return False
        infer = False
        new_possible_courses = []
        for course in self.ap.possible_courses:
            if self.ap.preReqMet(course,self.st.passedCourses):
                new_possible_courses.append(course)
            else:
                infer = True
        self.ap.possible_courses = new_possible_courses
        return infer

    # rule 3 - add the course with the most prerequisites to recomended courses
    def year2hrule3_transferHighestPreReq_15ECT(self):
        if self.ap.planYear!= 1 and self.ap.possible_courses != [] and self.ap.creditsRecomendedCourses() <= 15 and not self.ap.checkedPracticalCourses:
            self.ap.recommended_courses.append(self.ap.highestPreReg())
            return True
        else:
            return False

    # rule 4 - add the course with the most prerequisites to recommend course if lower than 20 ect
    def year2hrule4_transferHighestPreReq_20ECT(self):
        if self.ap.planYear!= 1 and self.ap.possible_courses != [] and self.ap.creditsRecomendedCourses() <= 20 and \
            self.ap.recommended_Extra5ECTS and not self.ap.checkedPracticalCourses:
            self.ap.recommended_courses.append(self.ap.highestPreReg())
            return True
        else:
            return False

    # rule 5 - add the pratical courses to possible courses after we checked mandatory courses in the case we need 15 credits
    def year2hrule5_checkedPracticals15(self):
        if self.ap.checkedMandatoryCourses and not self.ap.checkedPracticalCourses and self.ap.possible_courses == [] and \
        self.ap.creditsRecomendedCourses() <= 15:
            practicals = self.courses.getPracticalCourses(self.ap.planBlock)
            for course in practicals:
                self.ap.possible_courses.append(course)
            self.ap.checkedPracticalCourses = True
            return True
        else:
            return False

    # rule 6 - add the pratical courses to possible courses after we checked mandatory courses in the case that we need 20 credits 
    def year2hrule6_checkedPracticals20(self):
        if self.ap.checkedMandatoryCourses and not self.ap.checkedPracticalCourses and self.ap.possible_courses == [] and \
        self.ap.creditsRecomendedCourses() <= 20 and self.ap.recommended_Extra5ECTS:
            practicals = self.courses.getPracticalCourses(self.ap.planBlock)
            for course in practicals:
                self.ap.possible_courses.append(course)
            self.ap.checkedPracticalCourses = True
            return True
        else:
            return False

    # rule 7 - add practical with highest grade for pre reqs
    def year2hrule7(self):
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() <= 15 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses != []:
            self.ap.recommended_courses.append(self.ap.highestPreReqGrade())
            return True
        else:
            return False

    # rule 8 - put electives in possible courses if still lower than 15 credits
    def year2hrule8(self):
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() <= 15 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses == [] and not self.ap.recommended_Extra5ECTS:
            electives  = self.courses.getElectiveCourses(self.ap.planBlock)
            for course in electives:
                self.ap.possible_courses.append(course)
            self.ap.checkedElectiveCourses = True               
            return True
        else:
            return False
        
    # rule 9 - put electives in possible courses if still lower than 20 credits given that we recomend 5 extra credits
    def year2hrule9(self):
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() <= 20 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses == [] and self.ap.recommended_Extra5ECTS:
            electives  = self.courses.getElectiveCourses(self.ap.planBlock)
            for course in electives:
                self.ap.possible_courses.append(course)
            self.ap.checkedElectiveCourses = True               
            return True
        else:
            return False
        
    # rule 10 - if the student's orientation is cs, move the non-cs courses from the possible courses to other available electives
    def year2hrule10_moveNONCSCourses(self):
        if self.ap.checkedElectiveCourses == True and self.ap.planYear != 1 and self.st.getOrientation() == 2:
            for course in self.ap.possible_courses:
                if course.orientation == 1 and course.block == self.ap.planBlock:
                    self.ap.other_available_electives.append(course)
            self.ap.finishedElectives = True
            return True
        else:
            return False

    # rule 11 - if the student's orientation is non-cs, move the cs courses from the possible courses to other available electives
    def year2hrule11_moveCSCourses(self):
        if self.ap.checkedElectiveCourses == True and self.ap.planYear != 1 and self.st.getOrientation() == 1:
            for course in self.ap.possible_courses:
                if course.orientation == 2 and course.block == self.ap.planBlock:
                    self.ap.other_available_electives.append(course)
            self.ap.finishedElectives = True
            return True
        else:
            return False

    # rule 12 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule12_presentAdvice1(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits >= 15 and self.ap.recommended_Extra5ECTS == False:
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = False
            self.ap.finished = True
            return True
        else:
            return False


    # rule 13 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule13_presentAdvice2(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits() >= 20 and self.ap.recommended_Extra5ECTS == True:
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = False
            self.ap.finished = True
            return True
        else:
            return False

    # rule 14 - if the credits of the current scheduled courses are not enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule14_presentAdvice3(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits() <= 15 and self.ap.recommended_Extra5ECTS == False:
            self.ap.showOtherCourses = True
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = True
            self.ap.finished = True
            return True
        else:
            return False

    # rule 15 - if the credits of the current scheduled courses are not enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule15_presentAdvice4(self):
        if self.ap.finishedElectives == True and self.ap.totalCredits() <= 20 and self.ap.recommended_Extra5ECTS == True:
            self.ap.showOtherCourses = True
            self.ap.recommended_electives.append(self.ap.possible_courses)
            self.ap.showOtherCourses = True
            self.ap.finished = True
            return True
        else:
            return False
    
    # rule 16 - if the planning is for the first block of the third or higher year and requirements to start the Bachelor Project are met, recommend it  
    def year2hrule16_addBachelorProjectAIn1A(self):
        passedCourses = self.st.getPassedCourses()
        if self.ap.planYear >= 3 and self.ap.planBlock == 1 and self.st.calculateCurrentECTS >= 135 and \
        self.st.determinePropaedeuticPhasePassed == True and "Statistics" in passedCourses and \
        "Data Analytics and Communication" in passedCourses and self.ap.checkedMandatoryCourses == True and \
        self.ap.checkedPracticalCourses == True and self.st.startedBachelorProject == False:
            self.ap.recommended_courses.append("Bachelor Project A")
            return True
        else:
            return False

    # rule 17 - if the planning is for the second block and the Bachelor Project is already started, recommend it  
    def year2hrule17_addBachelorProjectBIn1B(self):
        if self.ap.planYear >= 3 and self.ap.planBlock == 2 and self.ap.checkedMandatoryCourses == False and \
        self.ap.checkedPracticalCourses == False and self.st.startedBachelorProject == True:
            self.ap.recommended_courses.append("Bachelor Project B")
            return True
        else:
            return False
    

    # rule 18 - if the planning is for the third block and requirements to start the Bachelor Project are met, recommend it  
    def year2hrule18_addBachelorProjectAIn2A(self):
        passedCourses = self.st.getPassedCourses()
        if self.ap.planBlock == 3 and self.st.calculateCurrentECTS >= 135 and \
        self.st.determinePropaedeuticPhasePassed == True and "Statistics" in passedCourses and \
        "Data Analytics and Communication" in passedCourses and self.ap.checkedMandatoryCourses == True and \
        self.ap.checkedPracticalCourses == True and self.st.startedBachelorProject == False:
            self.ap.recommended_courses.append("Bachelor Project A")
            return True
        else:
            return False

    # rule 19 - if the planning is for the fourth block and the Bachelor Project is already started, recommend it  
    def year2hrule19_addBachelorProjectBIn2B(self):
        if self.ap.planYear >= 3 and self.ap.planBlock == 4 and self.ap.checkedMandatoryCourses == False and \
        self.ap.checkedPracticalCourses == False and self.st.startedBachelorProject == True:
            self.ap.recommended_courses.append("Bachelor Project B")
            return True
        else:
            return False
        
    def doInference(self):
        infer = True
        fList = [self.allrule8,self.year1rule1_isAdvised,self.year1rule2_MandatoryRecomendation,self.year1rule3_highestPossiblePreRequisites,self.year1rule4_deleteNonCSCoursesWithLowGrades\
            ,self.year1rule5_deleteCSCoursesWithLowGrades,self.year1rule6_deleteNotMandatory,self.year1rule7_addDutchCourses,self.year1rule8_addEnglishCourses\
            ,self.year1rule9_addExtra5ECTS,self.year2hrule1_year2mandatory,self.year2hrule2_deleteNotPossible,self.year2hrule3_transferHighestPreReq_15ECT\
            ,self.year2hrule4_transferHighestPreReq_20ECT,self.year2hrule5_checkedPracticals15,self.year2hrule6_checkedPracticals20,self.year2hrule7\
            ,self.year2hrule8,self.year2hrule9,self.year2hrule10_moveNONCSCourses,self.year2hrule11_moveCSCourses,self.year2hrule12_presentAdvice1,self.year2hrule13_presentAdvice2\
            ,self.year2hrule14_presentAdvice3,self.year2hrule15_presentAdvice4,self.year2hrule16_addBachelorProjectAIn1A,self.year2hrule17_addBachelorProjectBIn1B\
            ,self.year2hrule18_addBachelorProjectAIn2A,self.year2hrule19_addBachelorProjectBIn2B,self.allrule1_practicalNoPreReq,self.allrule2_recommend5ECTS1\
            ,self.allrule3_recommend5ECTS2,self.allrule4_notRecommend5ECTS]
        while infer:
            infer = False
            for f in fList:
                if f():
                    print(f)
                    infer = True
        return
