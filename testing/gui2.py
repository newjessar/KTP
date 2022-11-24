

import PySimpleGUI as sg
from advisorySystem import Advisory
from courses import Courses

class GuiStudentInfo(object):
    
    def __init__(self, advisory : Advisory):
        self.advisory = advisory
        self.coursesList = self.advisory.yearTwoeC
        self.titleList = []
        
        for item in range(len(self.coursesList)):
            self.titleList.append(self.coursesList[item].getTitle())

    # Design pattern 2 - First window remains active
    def btxt(self, button_text):
        return sg.Button(button_text, size=(5, 1), font=("Helvetica", 20))
    
    # Design pattern 2 - First window remains active
    def ctxt(self, checkBox_text):
        return sg.Checkbox(checkBox_text, size=(5, 1), font=("Helvetica", 20))

    # Design pattern 1 - First window does not remain active
    def makeLayout(self):

        # Design pattern 1 - First window does not remain active

        layout_MainPage = [[sg.T('Student Advisory Application', font='_ 20', justification='c', expand_x=True)],
                [ sg.Text('Welcome to the system, please fill in your information by first clicking on the "Student Info" button', font='_ 18'),],
                # [sg.Input(do_not_clear=True)],
                # [sg.Text(size=(15,1),  key='-OUTPUT-')],
                [sg.Button('Student INFO'), sg.Button('Advisory')],
                [sg.Button('Resit'), sg.Button('Exit')]
                ]
        
        column_2 = [[sg.Button('Do Stuff', size=(14, 1))],
            [sg.Button('Do Other Stuff', size=(14, 1))],
            [sg.Text('Some text')]]
        
        layout_stuInfoFrame = [
                [sg.Frame('Student Information', layout_MainPage, font='_ 30')],
                # [sg.Submit('Confirm'), sg.Cancel('Cancel')]
                ]
        
        win1 = sg.Window('The PySimpleGUI Element List', layout_stuInfoFrame,size=(1200, 800))
        
        win2_active=False
        while True:
            ev1, vals1 = win1.read(timeout=100)
            if ev1 == sg.WIN_CLOSED or ev1 == 'Exit':
                break
            # win1.FindElement('-OUTPUT-').update(vals1[0])

            if ev1 == 'Student INFO'  and not win2_active:
                win2_active = True
                win1.Hide()
                layout_stuInfo = [[sg.T('Student Information', font='_ 30', justification='c', expand_x=True)],
                        [sg.Text('Please fill in your information then click the "Confirm" button', font='_ 18')],       
                        [[sg.Checkbox(t), ] for t in self.titleList],
                        [sg.Button('Select All'), sg.Button('Clear')]]
                layout_stuInfoFrame = [
                            [sg.Frame('Student Information', layout_stuInfo, font='_ 30')],
                            [sg.Submit('Confirm'), sg.Cancel('Cancel')]
                            ]
        
                        
    # Run the GUI
                win2 = sg.Window('Window 2', layout_stuInfoFrame, size=(1200, 800))
                while True:
                    ev2, vals2 = win2.read()
                    if ev2 == sg.WIN_CLOSED or ev2 == 'Cancel' or ev2 == 'Confirm':
                        win2.close()
                        win2_active = False
                        win1.UnHide()
                        break



