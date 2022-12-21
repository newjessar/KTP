#  class course facilitated by class courses

class Course(object):
    
    def __init__(self, id, title, orientation, pre_requ_cour, advised, year, block, mandatory, elective, practical, language, pre_requisite):
        self.id            = id             # int
        self.title         = title          # String
        self.orientation   = orientation    # int
        self.pre_requ_cour = pre_requ_cour  # Array
        self.advised       = advised        # Array
        self.year          = year           # int
        self.block         = block          # int
        self.strength      = int            # int
        self.mandatory     = mandatory      # Binary
        self.elective      = elective       # Binary
        self.practical     = practical      # Binary
        self.pre_requisite = pre_requisite  # Binary
        self.language      = language       # Binary


        
        
    def setStrength(self, x):
        self.strength = x
    
    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getOrientation(self):
        return self.orientation
    
    def getpre_requ_cour(self):
        return self.pre_requ_cour
    
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