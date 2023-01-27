#  class course facilitated by class courses

class Course(object):
    
    def __init__(self, id, title, orientation, pre_requ_cour, advised, year, block,credit, mandatory, elective,
    practical, language, pre_requisite, n_pre_req):
        self.id                     = id             # int
        self.title                  = title          # String
        self.orientation            = orientation    # int - orientation, = (Non-CS): 1 -- (CS): 2
        self.pre_requisite_courses  = pre_requ_cour  # Array
        self.advised_courses        = advised        # Array
        self.year                   = year           # int
        self.block                  = block          # int
        self.grade                  = -1.0            # int
        self.credit                 = credit         # int  
        self.mandatory              = mandatory      # Binary
        self.elective               = elective       # Binary
        self.practical              = practical      # Binary
        self.pre_requisite          = pre_requisite  # Binary
        self.language               = language       # Binary
        self.n_pre_req              = n_pre_req      # int


        
        
    def setStrength(self, x):
        self.strength = x

    def setPre_requisite(self, x):
        self.pre_requisite = x

    def setPre_requisite_courses(self, x):
        self.pre_requisite_courses = x
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getOrientation(self):
        return self.orientation
    
    def getpre_requ_cour(self):
        return self.pre_requisite_courses
    
    def getYear(self):
        return self.year
    
    def getBlock(self):
        return self.block
    
    def getStrength(self):
        return self.strength
    
    def getMandatory(self):
        return self.mandatory
    
    def getElective(self):
        return self.elective
    
    def getPractical(self):
        return self.practical
    
    def getPre_requisite(self):
        return self.pre_requisite
