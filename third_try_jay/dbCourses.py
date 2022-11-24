import numpy as np

class CoursesDB:
    # ID, title, orientation, pre-requisite, year, block, mandatory, elective, practical, pre_requisite
    # orientation = Alpha(Theoretical): 1 -- Bet(Logical): 2
    courses = np.array([    [0, "Improg" , 2, [], 1, 1, True, False, False, False],
                            [1, "Calculus", 2, [], 1, 2, True, False, False, False],
                            [2, "Introduction to logic", 2, [], 1, 2, True, False, False, False],
                            [3, "Cognitive Psychology", 1, [], 1, 3, True, False, False, False],
                            [4, "Introduction to Linguistics", 1, [], 1, 4, True, False, False, False],
                            [5, "Language Speech Technology", 2, [1, 4], 2, 2, False, True, False, True],
                            [6, "Advance Logic", 2, [2], 2, 3, True, False, False, True],
                            [7, "Language Speech Technology Practical", 2, [4], 2, 4, False, True, True, True],
                            [8, "Human Error" , 1, [], 3, 2, False, True, False, False]
                            ], dtype='object')
    np.save('courses_DB.npy', courses, allow_pickle=True)

    

        


    
    