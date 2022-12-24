

class Academic_planning:

    def __init__(self):
        self.recommended_courses = []
        self.possible_courses = []
        self.recommended_electives = []
        self.other_available_electives = []
        self.recommended_Extra5ECTS = bool
        self.finished = False
        self.finishedElectives = bool
        self.planYear = int
        self.planBlock = int
        self.showOtherCourses = bool
        self.checkedElectiveCourses = bool
        self.checkedMandatoryCourses = bool
        self.checkedPracticalCourses = bool


    def highestPreReg(self):
        preReq = -1
        coursePre = None
        for course in self.possible_courses:
            if (course.n_pre_req > preReq):
                 coursePre = course
                 preReq = course.n_pre_req               
        return coursePre

    def creditsRecomendedCourses(self):
        self.recommended_courses_ECTS = 0
        for course in self.recommended_courses:
            self.recommended_courses_ECTS += course.credit
        return self.recommended_courses_ECTS

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
            total += course.grade
        return total/len(courses)