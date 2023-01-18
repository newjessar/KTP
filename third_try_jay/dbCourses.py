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
    # n_pre_req, integer

    courses = np.array([    [0, "Imperative Programming (for AI)" , 2, [], [], 1, 1, 5, True, False, False, True, False, 1],
                            [1, "Calculus for Artificial Intelligence", 2, [], [], 1, 2, 5, True, False, False, True, False, 2],
                            [2, "Autonomous Systems", 2, [], [], 1, 1, 5, True, False, False, True, False, 1],
                            [3, "Introduction to Artificial Intelligence", 1, [], [], 1, 1, 5, True, False, False, True, False, 0],
                            [4, "Basic Scientific Skills", 2, [], ["Introduction to Artificial Intelligence"], 1, 2, 5, True, False, False, True, False,3],
                            [5, "Introduction to Logic (AI)", 2, [], [], 1, 2, 5, True, False, False, True, False, 1],

                            [6, "Algorithms and Data Structures (AI)", 2, [], ["Imperative Programming (for AI)"], 1, 3, 5, True, False, False, True, False, 0],
                            [7, "Cognitive Psychology", 1, [], [], 1, 3, 5, True, False, False, True, False, 2],
                            [8, "General Linguistics", 1, [], [], 1, 3, 5, True, False, False, True, False, 2],
                            [9, "Artificial Intelligence 1", 2,  [], ["Imperative Programming (for AI)", "Introduction to Logic (AI)", "Algorithms and Data Structures (AI)"], 1, 4, 5, True, False, False, True, False, 1],
                            [10, "Introduction to the Brain", 1, [], [], 1, 4, 5, True, False, False, True, False, 0],
                            [11, "Linear Algebra and Multivariable Calculus", 2, [], ["Calculus for Artificial Intelligence"], 1, 4, 5, True, False, False, True, False, 4],
                            
                            [12, "Language and Speech Technology", 2, ["General Linguistics","Calculus for Artificial Intelligence"], [], 2, 1, 5, True, False, False, True, True,1],
                            [13, "Knowledge and Agent Technology", 2, [], [], 2, 1, 5, True, False, False, True, False,0],
                            [14, "Statistics", 2, [], [], 2, 1, 5, True, False, False, True, False, 2],
                            
                            [15, "Architectures of Intelligence", 2, [], ["Cognitive Psychology"], 2, 2, 5, True, False, False, True, True, 1],
                            [16, "Signals and Systems (for AI)", 2, ["Calculus for Artificial Intelligence", "Linear Algebra and Multivariable Calculus"], ["Imperative Programming (for AI)"], 2, 2, 5, True, False, False, True, True, 1],
                            [17, "Data Analytics and Communication", 2, [], ["Statistics"], 2, 2, 5, True, False, False, True, True, 1],

                            [18, "Philosophy of AI and Cognition" , 1, [], [], 2, 3, 5, True, False, False, True, False, 0],
                            [19, "Advanced Logic", 2, ["Introduction to Logic (AI)"], [], 2, 3, 5, True, False, False, True, True, 0],
                            [20, "Cognition and attention" , 1, [], [], 2, 3, 5, False, True, False, True, False, 0],
                            [21, "Computer Graphics" , 2, ["Calculus for Artificial Intelligence", "Linear Algebra and Multivariable Calculus"], [], 2, 3, 5, False, True, False, True, True, 0],
                            [22, "Introduction to Information Systems", 2, [], ["Introduction to Logic (AI)"], 2, 3, 5, False, True, False, True, False, 0],
                            [23, "Agent Technology Practical" , 2, [], ["Object-Oriented Programming (for AI)"], 2, 3, 5, False, False, True, True, False, 0],
                            [24, "Cognitive Modelling Practical" , 1, ["Cognitive Psychology","Statistics","Architectures of Intelligence"], [], 2, 3, 5, False, False, True, True, True, 0],
                            [25, "Robotics Practical 1" , 2, ["Calculus for Artificial Intelligence","Linear Algebra and Multivariable Calculus"], ["Statistics","Imperative Programming (for AI)","Autonomous Systems","Signals and Systems (for AI)","Neural Networks"], 2, 3, 5, False, False, True, True, True, 0],

                            [26, "Ethics in Artificial Intelligence" , 1, [], [], 2, 4, 5, True, False, False, True, False, 0],
                            [27, "Neural Networks" , 2, ["Calculus for Artificial Intelligence","Linear Algebra and Multivariable Calculus"], [], 2, 4, 5, True, False, False, True, True, 0],
                            [28, "Object-Oriented Programming (for AI)" , 2, [], ["Imperative Programming (for AI)"], 2, 4, 5, True, False, False, True, False, 0],
                            
                            [29, "Artificial Intelligence 2" , 2 , [], ["Artificial Intelligence 1","Statistics"], 3, 1, 5, True, False, False, True, False, 0],
                            [30, "Advanced Object Oriented Programming" , 2, [], ["Object-Oriented Programming (for AI)"], 3, 1, 5, False, True, False, True, False, 0],
                            [31, "C++ fundamentals" , 2, ["Imperative Programming (for AI)","Object-Oriented Programming (for AI)"], [], 3, 1, 5, False, True, False, True, True, 0],
                            [32, "Computational Complexity" , 2, [], [], 3, 1, 5, False, True, False, True, False, 0],
                            [33, "Functional Programming" , 2, [], [], 3, 1, 5, False, True, False, True, False, 0],
                            [34, "Information Retrieval" , 2, [], ["Introduction to Information Systems","Algorithms and Data Structures (AI)"], 3, 1, 5, False, True, False, True, False, 0],
                            [35, "Information Security" , 2, [], [], 3, 1, 5, False, True, False, True, False, 0],
                            [36, "Introduction to Machine Learning" , 2, [], [], 3, 1, 5, False, True, False, True, False, 0],
                            [37, "Neurophysics (Physics for Artifician Intelligence)" , 2, ["Calculus for Artificial Intelligence","Linear Algebra and Multivariable Calculus","Signals and Systems (for AI)"], [], 3, 1, 5, False, True, False, True, True, 0],
                            [38, "Phil. of Mind: Body, Brain, Mind" , 1, [], [], 3, 1, 7, False, True, False, False, False, 0],
                            [39, "Structural Analysis of Language for Cognitive Modelling" , 1, ["General Linguistics"], [], 3, 1, 5, False, True, False, True, True, 0],
                            [40, "Cognitive Ergonomics Practical" , 1, ["Cognitive Psychology"], [], 3, 1, 5, False, False, True, True, True, 0],
                            
                            [41, "Compiler Construction" , 2, [], [], 3, 2, 5, False, True, False, True, False, 0],
                            [42, "Human Error" , 1, [], [], 3, 2, 5, False, True, False, True, False, 0],
                            [43, "IT Law for non-law students" , 1, [], [], 3, 2, 10, False, True, False, False, False, 0],
                            [44, "Introduction to Machine Learning (for AI)" , 2, ["Calculus for Artificial Intelligence","Linear Algebra and Multivariable Calculus"], [], 3, 2, 5, False, True, False, True, True, 0],
                            [45, "Introduction to Science Education" , 1, [], [], 3, 2, 5, False, True, False, False, False, 0],
                            [46, "Logic Programming" , 2, [], [], 3, 2, 5, False, True, False, True, False, 0],
                            [47, "Problem Analysis and Software Design" , 2, [], ["Object-Oriented Programming (for AI)"], 3, 2, 5, False, True, False, True, False, 0],
                            [48, "Programming in C++" , 2, [], ["C++ fundamentals"], 3, 2, 5, False, True, False, True, False, 0],
                            [49, "Web Engineering" , 2, [], ["Advanced Object Oriented Programming","Object-Oriented Programming (for AI)","Introduction to Information Systems"], 3, 2, 5, False, True, False, True, False, 0],
                            [50, "Knowledge Technology Practical" , 2, [], [], 3, 2, 5, False, False, True, True, False, 0],
                            [51, "Reinforcement Learning Practical" , 2, ["Autonomous Systems","Imperative Programming (for AI)"], [], 3, 2, 5, False, False, True, True, True, 0],

                            [52, "Advanced programming in C++" , 2, [], [], 3, 3, 5, False, True, False, True, False, 0],
                            [53, "Computational Grammar" , 1, ["Logic Programming"], [], 3, 3, 5, False, True, False, True, True, 0],
                            [54, "Philosophy of the Natural Sciences" , 1, [], [], 3, 3, 5, False, True, False, True, False, 0],

                            [55, "Advanced Algorithms and Data Structures" , 2, [], ["Object-Oriented Programming (for AI)","Algorithms and Data Structures (AI)"], 3, 4, 5, False, True, False, True, False, 0],
                            [56, "Human Factors" , 1, [], [], 3, 4, 5, False, True, False, True, False, 0],
                            [57, "Languages and Machines" , 2, [], ["Introduction to Logic (AI)"], 3, 4, 5, False, True, False, True, False, 0],
                            [58, "Parallel Computing" , 2, [], ["Imperative Programming (for AI)","Algorithms and Data Structures (AI)"], 3, 4, 5, False, True, False, True, False, 0],
                            [59, "Uncetainty in Machine Learning" , 2, [], ["Statistics"], 3, 4, 5, False, True, False, True, False, 0],
                            [60, "Language Technology Practical", 2, ["Language and Speech Technology"], [], 3, 4, 5, False, False, True, True, True, 0],
                            [61, "Robotics Practical 2" , 2, ["Calculus for Artificial Intelligence","Linear Algebra and Multivariable Calculus"],  ["Statistics","Imperative Programming (for AI)","Autonomous Systems","Signals and Systems (for AI)","Neural Networks","Robotics Practical 1"], 3, 4, 5, False, False, True, True, True, 0],

                            [62, "Bachelor's Project A" , 1, ["Data Analytics and Communication","Statistics"], [], 3, 5, 5, True, False, False, True, False, 0],
                            [63, "Bachelor's Project B", 1, ["Data Analytics and Communication","Statistics"], [], 3, 5, 10, True, False, False, True, False, 0]
                            


                            ], dtype='object')
    np.save('courses_DB.npy', courses, allow_pickle=True)

    

        


    
    
