
class Rules:
               
    def fourth_course(self):
        for wish in self.st.wishedCourses:
            if self.courList[wish].getOrientation() == self.st.getOrientation():
                if self.st.motivation > 7 :
                    self.advise = True
                    
    def above_four_course(self):
        for wish in self.st.wishedCourses:
            if self.courList[wish].getOrientation() == self.st.getOrientation():
                if self.st.motivation > 9 :
                    self.advise = True

    