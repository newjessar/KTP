
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
            for course2 in self.st.passedCourses:
                if course.title == course2.title:
                    course.grade = course2.grade
        self.courses.convertToCourses()
        self.courses.getAllYears()
        
        self.courList = self.courses.getAllcourses()
        self.yearOneC = self.courses.yearOneCour
        self.yearTwoC = self.courses.yearTwoCour
        self.yearThreeC = self.courses.yearThreeCour
        #self.advise = False
        self.examCommittee = "Contact the exam Committee"
        
    ## Rule Model

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
        #print(self.st.calculateAverageGrade())
        if self.st.want5ECTS and self.st.validReason() and self.st.failedCourses == 1 and self.st.calculateAverageGrade() >= 7 and self.ap.recommended_Extra5ECTS == None:
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
        if self.st.want5ECTS and self.ap.creditsRecomendedCourses() == 20  and not self.ap.finished:
            self.ap.finished = True
            return True
        else:
            return False

    # rule 6 - table 1 - all years
    def allrule6_notRecommend5ECTSAndFinish(self):
        if not self.st.want5ECTS and self.ap.creditsRecomendedCourses() == 15 and not self.ap.finished:
            self.ap.finished = True
            return True
        else:
            return False

    # rule 7 - table 1 - all years
    def allrule7_passed3Practicals(self):
        if self.ap.passedPracticals(self.st.passedCourses) and self.ap.changedPracticals==None:
            for course in self.courses.allcourses:
                if not (course.title in [passed.title for passed in self.st.passedCourses]) and course.practical == True\
                    and not (course.title in [passed.title for passed in self.ap.recommended_courses]):
                    course.practical = False
                    course.elective = True
                    self.ap.changedPracticals = True
            for course in self.ap.possible_courses:
                if course.practical == True:
                    course.practical = False
                    course.elective = True
                    self.ap.changedPracticals = True
                self.ap.possible_courses = []
            return True
        else:
            return False

    def allrule8(self):
        if self.st.orientation == None:
            orientation1_courses = []
            orientation2_courses = []
            for course in self.st.passedCourses:
                if course.orientation == 1:
                    orientation1_courses.append(course.grade)
                else: 
                    orientation2_courses.append(course.grade)
            orientation1 = self.ap.averageGrade(orientation1_courses)
            orientation2 = self.ap.averageGrade(orientation2_courses)
            if orientation2 > orientation1:
                self.st.orientation = 2
            else:
                self.st.orientation = 1
            return True
        else:
            return False


# ============ 1st Year Students ============
        
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
                passed = [x.title for x in self.st.passedCourses]
                if course.block == self.ap.planBlock and course.year != 1 and (all(x.title in passed for x in course.pre_requisite_courses)):
                    self.ap.possible_courses.append(course)
                    infer = True
        return infer
        
 # Rule 4 - if self.ap.planYear is 1 and self.ap.recommended_Extra5ECTS is true: 
    # then itterate through the courses in possible_courses to calculate the averageGrade of the courses with orientation: 1 
    # delete the courses with orientation 2 from the possible_courses if they are lower than the avrage of the courses with orientation 1
    def year1rule4_deleteNonCSCoursesWithLowGrades(self):
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and not self.ap.checkedOrientation and self.st.orientation == 2:
            new_pos = []
            for course in self.ap.possible_courses:
                if course.orientation == 2:
                    new_pos.append(course)
            self.ap.possible_courses = new_pos

            self.ap.checkedOrientation = True
            return True
        else:
            return False


# Rule 5 - if self.ap.planYear is 1 and self.ap.recommended_Extra5ECTS is true:     
   # Academic Planning year: recommendExtra5Credits is set to true &1st year & (averagegrade for cs courses < non cs courses)
   # Delete cs courses from possible courses.
    def year1rule5_deleteCSCoursesWithLowGrades(self):
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and not self.ap.checkedOrientation and self.st.orientation == 1:
            new_pos = []
            for course in self.ap.possible_courses:
                if course.orientation == 1:
                    new_pos.append(course)
            self.ap.possible_courses = new_pos

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
                self.ap.possible_courses = [y for y in self.ap.possible_courses if y.mandatory]
                infer = True
        return infer

  
# Rule 7 - not course.mandatory in (Academic planning possible courses) & and if self.ap.planYear is 1 and if the student speaks Dutch
# itterate through the possible courses and check if the course language is false.
# if the course language is false, add the course to the recommended courses
    def year1rule7_addDutchCourses(self): 
        infer = False
        if self.ap.planYear == 1 and self.st.language == False and self.ap.checkedLanguages == None and self.ap.possible_courses != [] and self.ap.noMandatoryCourseInPossibleCourses():
            for course in self.ap.possible_courses:
                if course.language == False:
                    self.ap.recommended_electives.append(course)
                    infer = True
                    self.ap.checkedLanguages = True
        return infer
        
        
# Rule 8 - if there are no mandatory courses in (Academic planning possible courses) & does not speak Dutch
    def year1rule8_addEnglishCourses(self): 
        infer = False
        if self.ap.planYear == 1 and self.st.language == True and self.ap.checkedLanguages == None and self.ap.possible_courses != [] and self.ap.noMandatoryCourseInPossibleCourses():
            for course in self.ap.possible_courses:
                if course.language == True:
                    self.ap.recommended_electives.append(course)
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

    def year1rule10_addExtra5ECTS(self):
        infer = False
        if self.ap.planYear == 1 and self.ap.recommended_Extra5ECTS and self.ap.creditsPossibleCourses() > 5 and not self.ap.noMandatoryCourseInPossibleCourses():
            self.ap.recommended_electives += (self.ap.possible_courses)
            self.ap.possible_courses = []
            self.ap.finished = True
            infer = True
        return infer
         

## 2nd+ Year Students
    # rule 1 - set all mandatory first year courses as recomended and put all mandatory second and third year courses as possible
    def year2hrule1_year2mandatory(self):
        if self.ap.recommended_courses == [] and self.ap.possible_courses == [] and self.ap.checkedMandatoryCourses==False:
            year1,year2,year3 = self.courses.getMandatoryBlockCourses(self.ap.planBlock)
            for course in year1:
                if self.st.notInPassed(course.title):
                    self.ap.recommended_courses.append(course)
            for course in year2:
                if self.st.notInPassed(course.title):                    
                    self.ap.possible_courses.append(course)                
            for course in year3:
                if self.st.notInPassed(course.title):
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
        new_recommended_courses = []
        for course in self.ap.recommended_courses:
            if self.ap.preReqMet(course,self.st.passedCourses):
                new_recommended_courses.append(course)
            else:
                infer = True
        self.ap.recommended_courses = new_recommended_courses
        new_recommended_courses = []
        for course in self.ap.recommended_electives:
            if self.ap.preReqMet(course,self.st.passedCourses):
                new_recommended_courses.append(course)
            else:
                infer = True
        self.ap.recommended_electives = new_recommended_courses
        return infer

    # rule 3 - add the course with the most prerequisites to recomended courses
    def year2hrule3_transferHighestPreReq_15ECT(self):
        #print([course.title for course in self.ap.possible_courses])
        if self.ap.planYear!= 1 and self.ap.possible_courses != [] and self.ap.creditsRecomendedCourses() < 15 and not self.ap.checkedPracticalCourses:
            self.ap.recommended_courses.append(self.ap.highestPreReg())
            return True
        else:
            return False

    # rule 4 - add the course with the most prerequisites to recommend course if lower than 20 ect
    def year2hrule4_transferHighestPreReq_20ECT(self):
        if self.ap.planYear!= 1 and self.ap.possible_courses != [] and self.ap.creditsRecomendedCourses() < 20 and \
            self.ap.recommended_Extra5ECTS and not self.ap.checkedPracticalCourses:
            print([course.title for course in self.ap.possible_courses])
            self.ap.recommended_courses.append(self.ap.highestPreReg())
            return True
        else:
            return False

    # rule 5 - add the pratical courses to possible courses after we checked mandatory courses in the case we need 15 credits
    def year2hrule5_checkedPracticals15(self):
        if self.ap.checkedMandatoryCourses and not self.ap.checkedPracticalCourses and self.ap.possible_courses == [] and \
        self.ap.creditsRecomendedCourses() < 15: 
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
        self.ap.creditsRecomendedCourses() < 20 and self.ap.recommended_Extra5ECTS:
            practicals = self.courses.getPracticalCourses(self.ap.planBlock)
            for course in practicals:
                self.ap.possible_courses.append(course)
            self.ap.checkedPracticalCourses = True
            return True
        else:
            return False

    # rule 7 - add practical with highest grade for pre reqs
    def year2hrule7(self):
        course = self.ap.highestPreReqGradeNoPop()
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() < 15 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses != [] and not self.ap.recommended_Extra5ECTS and\
            course.orientation == self.st.orientation:
            course = self.ap.highestPreReqGrade()
            self.ap.recommended_courses.append(course)
            return True
        else:
            return False
        
    def year2hrule8(self):
        course = self.ap.highestPreReqGradeNoPop()
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() < 15 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses != [] and not self.ap.recommended_Extra5ECTS and\
            course.orientation != self.st.orientation:
            course = self.ap.highestPreReqGrade()
            self.ap.recommended_electives.append(course)
            return True
        else:
            return False

    def year2hrule9(self):
        course = self.ap.highestPreReqGradeNoPop()
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() < 20 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses != [] and self.ap.recommended_Extra5ECTS and\
            course.orientation == self.st.orientation:
            course = self.ap.highestPreReqGrade()
            self.ap.recommended_courses.append(course)
            return True
        else:
            return False
        
    def year2hrule10(self):
        course = self.ap.highestPreReqGradeNoPop()
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() < 20 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses != [] and self.ap.recommended_Extra5ECTS and\
            course.orientation != self.st.orientation:
            course = self.ap.highestPreReqGrade()
            self.ap.recommended_electives.append(course)
            return True
        else:
            return False

    # rule 9 - put electives in possible courses if still lower than 15 credits
    def year2hrule11(self):
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() < 15 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses == [] and not self.ap.recommended_Extra5ECTS:
            electives  = self.courses.getElectiveCourses(self.ap.planBlock)
            for course in electives:
                self.ap.possible_courses.append(course)
            self.ap.checkedElectiveCourses = True               
            return True
        else:
            return False
        
    # rule 10 - put electives in possible courses if still lower than 20 credits given that we recomend 5 extra credits
    def year2hrule12(self):
        if self.ap.planYear !=1 and self.ap.creditsRecomendedCourses() < 20 and self.ap.checkedPracticalCourses and not self.ap.checkedElectiveCourses\
            and self.ap.possible_courses == [] and self.ap.recommended_Extra5ECTS:
            electives  = self.courses.getElectiveCourses(self.ap.planBlock)
            for course in electives:
                self.ap.possible_courses.append(course)
            self.ap.checkedElectiveCourses = True               
            return True
        else:
            return False
        
    # rule 11 - if the student's orientation is cs, move the non-cs courses from the possible courses to other available electives
    def year2hrule13_moveNONCSCourses(self):
        if self.ap.checkedElectiveCourses and self.ap.planYear != 1 and self.st.getOrientation() == 2 and not self.ap.finishedElectives:
            new_possible = []
            for course in self.ap.possible_courses:
                if course.language or not self.st.language:
                    if course.orientation == 1 and course.block == self.ap.planBlock:
                        self.ap.other_available_electives.append(course)
                    else:
                        new_possible.append(course)
            self.ap.possible_courses = new_possible
            self.ap.finishedElectives = True
            return True
        else:
            return False

    # rule 12 - if the student's orientation is non-cs, move the cs courses from the possible courses to other available electives
    def year2hrule14_moveCSCourses(self):
        if self.ap.checkedElectiveCourses and self.ap.planYear != 1 and self.st.getOrientation() == 1 and not self.ap.finishedElectives:
            #print([course.title for course in self.ap.possible_courses])

            new_possible = []
            for course in self.ap.possible_courses:
                #print(course.title)
                if course.language or not self.st.language:
                    if course.orientation == 2:
                        self.ap.other_available_electives.append(course)
                    else:
                        new_possible.append(course)
            self.ap.possible_courses = new_possible
            self.ap.finishedElectives = True
            #print([course.title for course in self.ap.possible_courses])
            #print([course.title for course in self.ap.other_available_electives])
            return True
        else:
            return False

    # rule 13 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule15_presentAdvice1(self):
        if self.ap.finishedElectives and self.ap.totalCredits() >= 15 and not self.ap.recommended_Extra5ECTS and not self.ap.finished:
            self.ap.recommended_electives += self.ap.possible_courses
            self.ap.showOtherCourses = False
            self.ap.finished = True
            return True
        else:
            return False


    # rule 14 - if the credits of the current scheduled courses are enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule16_presentAdvice2(self):
        if self.ap.finishedElectives and self.ap.totalCredits() >= 20 and self.ap.recommended_Extra5ECTS and not self.ap.finished:
            self.ap.recommended_electives += self.ap.possible_courses
            self.ap.showOtherCourses = False
            self.ap.finished = True
            return True
        else:
            return False

    # rule 15 - if the credits of the current scheduled courses are not enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule17_presentAdvice3(self):
        if self.ap.finishedElectives and self.ap.totalCredits() <= 15 and not self.ap.recommended_Extra5ECTS and not self.ap.finished:
            self.ap.showOtherCourses = True
            self.ap.recommended_electives += self.ap.possible_courses
            self.ap.finished = True
            return True
        else:
            return False

    # rule 16 - if the credits of the current scheduled courses are not enough, then add other possible courses to the recommended electives, and present the advice to students
    def year2hrule18_presentAdvice4(self):
        if self.ap.finishedElectives and self.ap.totalCredits() <= 20 and self.ap.recommended_Extra5ECTS and not self.ap.finished:
            self.ap.showOtherCourses = True
            self.ap.recommended_electives += self.ap.possible_courses
            self.ap.finished = True
            return True
        else:
            return False
    
    # rule 17 - if the planning is for the first block of the third or higher year and requirements to start the Bachelor Project are met, recommend it  
    def year2hrule19_addBachelorProjectAIn1A(self):
        passedCourses = self.st.getPassedCourses()
        if self.ap.planYear >= 3 and self.ap.planBlock == 1 and self.st.calculateCurrentECTS() >= 135 and \
        self.st.determinePropaedeuticPhasePassed() == True and "Statistics" in [course.title for course in passedCourses] and \
        "Data Analytics and Communication" in [course.title for course in passedCourses] and self.ap.checkedMandatoryCourses == True and \
        self.ap.checkedPracticalCourses == True and self.st.startedBachelorProject == False  and self.ap.notInRecommended("Bachelor's Project A"):
            for course in self.courses.allcourses:
                if (course.title=="Bachelor's Project A"):
                    self.ap.recommended_courses.append(course)
            return True
        else:
            return False

    # rule 18 - if the planning is for the second block and the Bachelor Project is already started, recommend it  
    def year2hrule20_addBachelorProjectBIn1B(self):
        if self.ap.planYear >= 3 and self.ap.planBlock == 2 and self.st.startedBachelorProject == True and \
            self.ap.notInRecommended("Bachelor's Project B"):
            for course in self.courses.allcourses:
                if (course.title=="Bachelor's Project B"):
                    self.ap.recommended_courses.append(course)
            return True
        else:
            return False
    

    # rule 19 - if the planning is for the third block and requirements to start the Bachelor Project are met, recommend it  
    def year2hrule21_addBachelorProjectAIn2A(self):
        passedCourses = self.st.getPassedCourses()
        if self.ap.planBlock >= 3 and self.st.calculateCurrentECTS() >= 135 and \
        self.st.determinePropaedeuticPhasePassed() == True and "Statistics" in [course.title for course in passedCourses] and \
        "Data Analytics and Communication" in [course.title for course in passedCourses] and self.ap.checkedMandatoryCourses == True and \
        self.ap.checkedPracticalCourses == True and self.st.startedBachelorProject == False  and self.ap.notInRecommended("Bachelor's Project A"):
            for course in self.courses.allcourses:
                if (course.title=="Bachelor's Project A"):
                    self.ap.recommended_courses.append(course)
            return True
        else:
            return False

    # rule 20 - if the planning is for the fourth block and the Bachelor Project is already started, recommend it  
    def year2hrule22_addBachelorProjectBIn2B(self):
        if self.ap.planYear >= 3 and self.ap.planBlock == 4 and self.st.startedBachelorProject == True and \
            self.ap.notInRecommended("Bachelor's Project B"):
            for course in self.courses.allcourses:
                if (course.title=="Bachelor's Project B"):
                    self.ap.recommended_courses.append(course)
            return True
        else:
            return False

    def year2hrule23_noDutch(self):
        infer = False
        if self.ap.planYear != 1 and self.st.language:
            new_poss = []
            for course in self.ap.recommended_electives:
                if course.language:
                    new_poss.append(course)
                else:
                    infer=True
            self.ap.recommended_electives = new_poss
            new_poss = []
            for course in self.ap.possible_courses:
                if course.language:
                    new_poss.append(course)
                else:
                    infer=True
            self.ap.possible_courses = new_poss
        return infer
        
    def doInference(self):
        infer = True
        fList = [self.allrule2_recommend5ECTS1\
            ,self.allrule3_recommend5ECTS2,self.allrule4_notRecommend5ECTS,self.allrule5_recommend5ECTSAndFinish,self.allrule6_notRecommend5ECTSAndFinish\
            ,self.allrule7_passed3Practicals,self.allrule8,self.year1rule2_MandatoryRecomendation,self.year1rule3_highestPossiblePreRequisites,self.year1rule4_deleteNonCSCoursesWithLowGrades\
            ,self.year1rule5_deleteCSCoursesWithLowGrades,self.year1rule6_deleteNotMandatory,self.year1rule7_addDutchCourses,self.year1rule8_addEnglishCourses\
            ,self.year1rule9_addExtra5ECTS,self.year2hrule1_year2mandatory,self.year2hrule2_deleteNotPossible,self.year2hrule3_transferHighestPreReq_15ECT\
            ,self.year2hrule4_transferHighestPreReq_20ECT,self.year2hrule5_checkedPracticals15,self.year2hrule6_checkedPracticals20,self.year2hrule7\
            ,self.year2hrule8,self.year2hrule9,self.year2hrule10,self.year2hrule11,self.year2hrule12,self.year2hrule13_moveNONCSCourses,\
            self.year2hrule14_moveCSCourses,self.year2hrule15_presentAdvice1,self.year2hrule16_presentAdvice2\
            ,self.year2hrule17_presentAdvice3,self.year2hrule18_presentAdvice4,self.year2hrule19_addBachelorProjectAIn1A,self.year2hrule20_addBachelorProjectBIn1B\
            ,self.year2hrule21_addBachelorProjectAIn2A,self.year2hrule22_addBachelorProjectBIn2B,self.year1rule10_addExtra5ECTS,self.year2hrule23_noDutch]

        while infer:
            infer = False
            for f in fList:
                if f():
                    print(f)
                    infer = True
        return
