# passed courses

import numpy as np
from course import Course
from dbCourses import CoursesDB

class Courses(object):
    
    def __init__(self):
        self.dbCoursess    = CoursesDB()
        self.allcourses    = []
        self.yearOneCour   = []
        self.yearTwoCour   = []
        self.yearThreeCour = []        

    def initiateCourses(self):
        loadcourses = np.load('courses_DB.npy', allow_pickle=True)
        for i in loadcourses:
            self.allcourses.append(Course(i[0], i[1], i[2], i[3], 
                                            i[4], i[5], i[6], i[7], 
                                            i[8], i[9], i[10], i[11],
                                            i[12], i[13]))
                
    def getAllcourses(self):
        return self.allcourses

    def convertToCourses(self):
        for course in self.allcourses:
            pre = course.pre_requisite_courses
            new_pre = []
            for pre_course in pre:
                for course2 in self.allcourses:
                    if pre_course == course2.title:
                        new_pre.append(course2)
            course.pre_requisite_courses = new_pre


    
    def getMandatoryBlockCourses(self,Block):
        year1 = []
        year2 = []
        year3 = []
        for course in self.yearOneCour:
            if course.mandatory and course.block == Block and course.grade==-1:
                year1.append(course)

        for course in self.yearTwoCour:
            if course.mandatory and course.block == Block and course.grade==-1:
                year2.append(course)

        for course in self.yearThreeCour:
            if course.mandatory and course.block == Block and course.grade==-1:
                year3.append(course)
        return year1,year2,year3

    def getPracticalCourses(self,Block):
        practicals = []
        for course in self.yearTwoCour:
            if course.practical and course.block == Block and course.grade==-1:
                practicals.append(course)

        for course in self.yearThreeCour:
            if course.practical and course.block == Block and course.grade==-1:
                practicals.append(course)
        return practicals

    def getElectiveCourses(self,Block):
        practicals = []
        for course in self.yearTwoCour:
            if course.elective and course.block == Block and course.grade==-1:
                practicals.append(course)

        for course in self.yearThreeCour:
            if course.elective and course.block == Block and course.grade==-1:
                practicals.append(course)
        return practicals

    # Clustering the courses base on years
    def getAllYears(self):
        self.yearOneCour = []
        self.yearTwoCour = []
        self.yearThreeCour = []
        for idx in range(len(self.allcourses)):   
            if self.allcourses[idx].getYear() == 1:
                self.yearOneCour.append(self.allcourses[idx])
            elif self.allcourses[idx].getYear() == 2:
                self.yearTwoCour.append(self.allcourses[idx])
            else:
                self.yearThreeCour.append(self.allcourses[idx])

    
