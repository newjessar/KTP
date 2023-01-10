
import numpy as np

class Academic_planning:

    def __init__(self):
        self.recommended_courses = []
        self.possible_courses = []
        self.recommended_electives = []
        self.other_available_electives = []
        self.recommended_Extra5ECTS = None
        self.finished = False
        self.finishedElectives = None
        self.planYear = None
        self.planBlock = None
        self.showOtherCourses = None
        self.checkedOrientation = False
        self.checkedElectiveCourses = None
        self.checkedMandatoryCourses = None
        self.checkedPracticalCourses = None
        self.checkedLanguages = None


    def highestPreReg(self):
        preReq = -1
        coursePre = None
        for course in range(len(self.possible_courses)):
            if (self.possible_courses[course].n_pre_req > preReq):
                 coursePre = course
                 preReq = course.n_pre_req
        highest_course = self.possible_courses.pop(coursePre)
        return highest_course

    def avgGradePreReq(course):
        grade = 0
        if (len(course.pre_requisite_courses)==0):
            return 0
        for pre in course.pre_requisite_courses:
            grade += pre.grade
        return grade/len(course.pre_requisite_courses)

    def highestPreReqGrade(self):
        preReq = -1
        coursePre = None
        for course in range(len(self.possible_courses)):
            avgGrade = self.avgGradePreReq(self.possible_courses[course])
            if (avgGrade > preReq):
                 coursePre = course
                 preReq = avgGrade
        highest_course = self.possible_courses.pop(coursePre)
        return highest_course

    def creditsRecomendedCourses(self):
        self.recommended_courses_ECTS = 0
        for course in self.recommended_courses:
            self.recommended_courses_ECTS += course.credit
        return self.recommended_courses_ECTS

    def creditsPossibleCourses(self):
        possCredits = 0
        for course in self.possible_courses:
            print(course.credit)
            possCredits += course.credit
        return possCredits

    def totalCredits(self):
        self.recommended_courses_ECTS = 0
        for course in self.recommended_courses:
            self.recommended_courses_ECTS += course.credit
        for course in self.recommended_electives:
            self.recommended_courses_ECTS += course.credit
        return self.recommended_courses_ECTS

    def preReqMet(self,course,passed_course):
        met = True
        for preReq in course.pre_requisite_courses:
            if not (preReq in passed_course):
                met = False
                return met
        return met
    
    # claclulate the avrage grades of an array of courses
    def averageGrade(self,courses):
        total = 0
        for course in courses:
            total += course
        if len(courses)==0:
            return 0
        return total/len(courses)
