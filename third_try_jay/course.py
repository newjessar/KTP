#  class course facilitated by class courses

class Course(object):
    
    def __init__(self, id, title, orientation, pre_requ_cour, year, block, mandatory, elective, practical, pre_requisite):
        self.id            = id
        self.title         = title
        self.orientation   = orientation
        self.pre_requ_cour = pre_requ_cour
        self.year          = year
        self.block         = block
        self.strength      = int
        self.mandatory     = mandatory
        self.elective      = elective
        self.practical     = practical
        self.pre_requisite = pre_requisite
        
        
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