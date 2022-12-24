import numpy as np

class CoursesDB:
    # ID, 
    # title, 
    # orientation, = Alpha(Non-CS): 1 -- Bet(CS): 2
    # pre-requisite-Courses, []
    # advised, []
    # year, 
    # block, 
    # Credits
    # mandatory, 
    # elective, 
    # practical, 
    # Language, = English: 1 -- Dutch: 0
    # pre_requisite, Binary
    #  n_pre_req, integer
    courses = np.array([    [0, "Improg" , 2, [], [], 1, 1, 5, True, False, False, False, False,2],
                            [1, "Calculus", 2, [], [], 1, 2, 5, True, False, False, False, False,3],
                            [2, "Introduction to logic", 2, [], [], 1, 2, 5, True, False, False, False, False,2],
                            [3, "Cognitive Psychology", 1, [], [], 1, 3, 5, True, False, False, False, False,0],
                            [4, "Introduction to Linguistics", 1, [], [], 1, 4, 5, True, False, False, False, False,0],
                            [5, "Language Speech Technology", 2, [1, 4], [], 2, 2, 5, False, True, False, True, False,2],
                            [6, "Advance Logic", 2, [2], [], 2, 3, 5, True, False, False, True, False,0],
                            [7, "Language Speech Technology Practical", 2, [4], [], 2, 4, 5, False, True, True, True, False,0],
                            [8, "Human Error" , 1, [], [], 3, 2, 5, False, True, False, False, False,0]
                            ], dtype='object')
    np.save('courses_DB.npy', courses, allow_pickle=True)

    

        


    
    
