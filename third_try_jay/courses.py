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
                                            i[8], i[9], i[10], i[11]))
                
    def getAllcourses(self):
        return self.allcourses
    
    def getMandatoryBlockCourses(self,Block):
        year1 = []
        year2 = []
        year3 = []
        for course in self.yearOneCour:
            if course.mandatory and course.block == Block:
                year1.append(course)

        for course in self.yearTwoCour:
            if course.mandatory and course.block == Block:
                year2.append(course)

        for course in self.yearThreeCour:
            if course.mandatory and course.block == Block:
                year3.append(course)
        return year1,year2,year3

    # Clustering the courses base on years
    def getAllYears(self):
        for idx in range(len(self.allcourses)):   
            if self.allcourses[idx].getYear() == 1:
                self.yearOneCour.append(self.allcourses[idx])
                # print("one", self.allcourses[idx].getTitle())
            elif self.allcourses[idx].getYear() == 2:
                self.yearTwoCour.append(self.allcourses[idx])
                # print("Two")
            else:
                self.yearThreeCour.append(self.allcourses[idx])
                # print("Three")

    