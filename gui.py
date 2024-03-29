# from courses import Courses
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import customtkinter
import numpy as np
from student import Student
from academic_planning import Academic_planning
from knowledge_Base import Knowledge_Base

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue")


class App(customtkinter.CTk):
    HEIGHT = 720
    WIDTH = 1300
    
    def __init__(self):
        super().__init__()
        self.ac = Academic_planning()
        self.kb = Knowledge_Base(Student())
        self.st = self.kb.st
        self.resizable(True, True)
        self.mainWindow()

    def mainWindow(self):
        # configure window
        self.title("Student Advisory Application.py")
        self.geometry(self.get_centered_geometry(self, App.HEIGHT, App.WIDTH))
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  # call .on_closing() when app gets closed
        self.seButtons = []
        self.change_appearance_mode("System")
        self.check_varsCourses = []
        self.gradeEentries = {}
        self.adviced_courses_titel = []

        # -----------------------------------  String variables  -----------------------------------
        self.stname_Var = customtkinter.StringVar(0, "Ex: John Smith, etc...")
        self.stNo_Var = customtkinter.StringVar(0, "Ex: s1234567, etc...")
        self.academicBlock_var = customtkinter.StringVar(value="1st Block")
        self.academicYear_var = customtkinter.StringVar(value="1st Year")
        self.doWant5ectsVar = customtkinter.StringVar(value="off")
        self.languageRadio_var = customtkinter.StringVar(value="on")
        self.reason5ects_var = customtkinter.StringVar(value="Choose a reason")
        self.followBScProject_var = customtkinter.StringVar(value="off")
        self.howManyFailedCourses_var = customtkinter.StringVar(0, value="0")

        # ============ create two frames (2x1) ============
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ frame_left
        # configure grid layout (1x15)

        self.frame_left = customtkinter.CTkFrame(master=self, corner_radius=5)
        self.frame_left.grid(row=0, column=0, sticky="nswe")
        self.frame_left.grid_columnconfigure(0, weight=1)
        self.frame_left.grid_rowconfigure((0, 1, 2, 4, 5, 6, 7, 9, 10, 11, 12), weight=0)
        self.frame_left.grid_propagate(False)


        self.si_StudentINFO_label_left = customtkinter.CTkLabel(master=self.frame_left,
                                                                text="Student INFO",
                                                                font=customtkinter.CTkFont(size=20, weight="bold"))
        self.si_StudentINFO_label_left.grid(row=0, column=0, pady=(20, 10), padx=10, sticky="n")

        self.si_Academic_Progress_button_left = customtkinter.CTkButton(master=self.frame_left,
                                                                        text="Academic Progress",
                                                                        command=lambda: self.academic_progress_Window(
                                                                            self.si_Academic_Progress_button_left))
        self.si_Academic_Progress_button_left.grid(row=1, column=0, pady=5, padx=5, sticky="n")

        # Name
        self.pr_SInfoName_label_left = customtkinter.CTkLabel(master=self.frame_left,
                                                              text="",
                                                              font=customtkinter.CTkFont(size=14, weight="bold"))
        self.pr_SInfoName_label_left.grid(row=2, column=0, pady=5, padx=5, sticky="s")

        # Number
        self.pr_SInfoNumber_label_left = customtkinter.CTkLabel(master=self.frame_left,
                                                                text="",
                                                                font=customtkinter.CTkFont(size=14, weight="bold"))
        self.pr_SInfoNumber_label_left.grid(row=3, column=0, pady=5, padx=5, sticky="s")
        # Year
        self.pr_SInfoYear_label_left = customtkinter.CTkLabel(master=self.frame_left,
                                                              text="",
                                                              font=customtkinter.CTkFont(size=14, weight="bold"))
        self.pr_SInfoYear_label_left.grid(row=4, column=0, pady=5, padx=5, sticky="s")
        # Block
        self.pr_SInfoBlock_label_left = customtkinter.CTkLabel(master=self.frame_left,
                                                               text="",
                                                               font=customtkinter.CTkFont(size=14, weight="bold"))
        self.pr_SInfoBlock_label_left.grid(row=5, column=0, pady=5, padx=5, sticky="s")
        # Average Grade
        self.pr_SInfoAverageGrade_label_left = customtkinter.CTkLabel(master=self.frame_left,
                                                                      text="",
                                                                      font=customtkinter.CTkFont(size=14,
                                                                                                 weight="bold"))
        self.pr_SInfoAverageGrade_label_left.grid(row=6, column=0, pady=5, padx=5, sticky="s")

        # ================== TreeView ==================
        self.treeView = customtkinter.CTkFrame(master=self.frame_left)
        self.treeView.grid(row=7, column=0, pady=2, padx=2, sticky="NSWE")
        self.treeView.grid_columnconfigure(0, weight=1)
        self.treeView.grid_rowconfigure(0, weight=1)
        self.treeView.grid_rowconfigure(0, weight=0)  # Added to allow the frame to shrink if necessary

        self.gradingTree = ttk.Treeview(self.treeView, columns=("c1", "c2"), show="headings", height=10)
        self.gradingTree.grid(row=0, column=0, pady=5, padx=5, sticky="NSWE")

        # add a vertical scrollbar to the treeview
        scrY = ttk.Scrollbar(self.treeView, orient="vertical", command=self.gradingTree.yview)
        scrY.grid(row=0, column=1, sticky="NS")
        self.gradingTree.configure(yscrollcommand=scrY.set)
        self.gradingTree.configure(yscrollcommand=scrY.set)

        self.gradingTree.heading("c1", text="Course")
        self.gradingTree.heading("c2", text="Grade")
        self.gradingTree.column("c1", width=120, anchor="center")
        self.gradingTree.column("c2", width=50, anchor="center")

        # ============ Help ============
        self.si_Reset_label_left = customtkinter.CTkButton(master=self.frame_left,
                                                           text="Reset",
                                                           command=self.reset_event)
        self.si_Reset_label_left.grid(row=9, column=0, pady=5, padx=5, sticky="s")

        # create help button
        self.si_help_button_left = customtkinter.CTkButton(master=self.frame_left,
                                                           text="Help",
                                                           command=self.show_help_popup)
        self.si_help_button_left.grid(row=10, column=0, pady=(5, 5), padx=5, sticky="s")

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=11, column=0, pady=5, padx=5, sticky="s")

        self.si_lds_label_left = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                             values=["Light", "Dark", "System"],
                                                             command=self.change_appearance_mode)
        self.si_lds_label_left.grid(row=12, column=0, pady=5, padx=5, sticky="s")

        # set default values
        self.si_lds_label_left.set("System")

        #  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  frame_right
        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, padx=20, pady=20, sticky="NSWE")
        self.frame_right.grid_columnconfigure(0, weight=1)
        self.frame_right.grid_rowconfigure(0, weight=1)
        self.frame_right.rowconfigure(0, weight=0)  # set weight of third row to be 5
        self.frame_right.rowconfigure(1, weight=1)  # set weight of third row to be 1

        self.frame_dash_Titel = customtkinter.CTkFrame(master=self.frame_right, corner_radius=10)
        self.frame_dash_Titel.grid(row=0, column=0, pady=5, padx=5, sticky="NSWE")
        self.frame_dash_Titel.grid_columnconfigure(1, weight=1)
        self.frame_dash_Titel.rowconfigure(0, weight=1)  # set weight of third row to be 1

        self.sd_StudentDashboard_label_right = customtkinter.CTkLabel(master=self.frame_dash_Titel,
                                                                      text="Student's Advisor",
                                                                      font=customtkinter.CTkFont(size=30,
                                                                                                 weight="bold"))  # font name and size in px
        self.sd_StudentDashboard_label_right.grid(row=0, column=1, columnspan=2, pady=10, padx=10, sticky="NWE")


        # ============ frame Advise explanation  ============
        self.frame_explanation = customtkinter.CTkFrame(master=self.frame_right, 
                                                        height=50,
                                                        corner_radius=10)
        self.frame_explanation.grid(row=4, column=0, pady=5, padx=5, sticky="NWE")
        self.frame_explanation.columnconfigure(0, weight=1)
        self.frame_explanation.rowconfigure(1, weight=1)

        self.pr_adviceExplanation_label_down = customtkinter.CTkLabel(master=self.frame_explanation,
                                                                      text="Reasons behind the advise:",
                                                                      font=customtkinter.CTkFont(size=20,
                                                                                                 weight="bold"))  # font name and size in px
        self.pr_adviceExplanation_label_down.grid(row=0, column=0, pady=5, padx=15, sticky="NWE")

        self.pr_textExplanation_textBox_down = customtkinter.CTkTextbox(master=self.frame_explanation,
                                                                        wrap=tkinter.WORD,
                                                                        height=50,
                                                                        font=customtkinter.CTkFont(size=15))
        self.pr_textExplanation_textBox_down.grid(row=1, column=0, pady=10, padx=10, sticky="NSEW")

            
            
    def show_help_popup(self):
        # create popup window
        popup = customtkinter.CTkToplevel(self)
        popup.title("Help")
        # popup.geometry("400x230")
        popup.geometry(self.get_centered_geometry(popup, 350,  410))
        popup.attributes("-topmost", True) # set the popup window on top of other windows
        
        # grab the mouse and keyboard events for the popup window
        popup.grab_set()

        # create label with help text
        help_text = "Guideness:\n" + \
                    "--------------------------- \n" + \
                    " 1- Click on Academic Progress. \n" + \
                    " 2- Fill up student information forme.  \n" + \
                    " 3- By filling the name and S-Number   \n" + \
                    "    the Process button will be active,   \n" + \
                    "    click it to activate Add the Grades. \n" + \
                    " 4- Choose the courses that you passed, \n" + \
                    "    navigating between the year's tab  \n" + \
                    "    will reveal you all the courses.\n" + \
                    " 5- Add the grades.\n" + \
                    " 6- Fill the courses preferences.\n" + \
                    " 6- Press save."
        help_label = customtkinter.CTkLabel(master=popup,
                                            text=help_text,
                                            corner_radius=6,
                                            fg_color=("white", "gray38"),
                                            font=customtkinter.CTkFont(size=20),
                                            justify=tkinter.LEFT,
                                            padx=10,
                                            pady=10)
        help_label.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="NSEW")

        def close_popup():
            popup.grab_release()
            popup.destroy()

        # bind the 'Escape' key to close the popup
        popup.bind('<Escape>', lambda event: close_popup())
        popup.protocol("WM_DELETE_WINDOW", close_popup)  # handle closing with the window's close button

        ############################################################################################################
        # ===================================== create Academic Prograss frame =====================================
        ############################################################################################################

    def academic_progress_Window(self, btn):
        btn.configure(state="disabled")
        self.ap_window = customtkinter.CTkToplevel(self)
        # Geometry  = WIDTH = 933 x HEIGHT = 720
        self.ap_window.geometry(self.get_centered_geometry(self.ap_window, App.HEIGHT, App.WIDTH))
        self.withdraw()
        self.ap_window.protocol("WM_DELETE_WINDOW", self.unhide_academic_progress_Window_event)
        self.ap_window.columnconfigure((0, 1, 2, 3, 4), weight=1)
        self.ap_window.rowconfigure((0, 1, 2, 3), weight=1)
        self.ap_window.title("Academic Progress")
        self.ap_window.resizable(True, True)

        # ----------------- Title -----------------
        self.ap_titel_label_base = customtkinter.CTkLabel(master=self.ap_window,
                                                          text="Academic Progress",
                                                          font=customtkinter.CTkFont(size=30,
                                                                                     weight="bold"))  # font name and size in px
        self.ap_titel_label_base.grid(row=0, column=0, columnspan=5, pady=5, padx=5, sticky="EW")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frame Left-A ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.frame_acWindow_left_A = customtkinter.CTkFrame(master=self.ap_window, corner_radius=5)
        self.frame_acWindow_left_A.grid(row=1, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="NSEW")
        self.frame_acWindow_left_A.columnconfigure((0, 1), weight=0)
        self.frame_acWindow_left_A.rowconfigure(1, weight=1)

        # Create the frame label
        self.ap_Studnet_Information_label_left = customtkinter.CTkLabel(master=self.frame_acWindow_left_A,
                                                                        text="Student Information",
                                                                        font=customtkinter.CTkFont(size=20,
                                                                                                   weight="bold"))  # font name and size in px
        self.ap_Studnet_Information_label_left.grid(row=0, column=0, columnspan=2, pady=5, padx=5, sticky="EW")

        # Create the name label
        self.ap_StudentName_label_left = customtkinter.CTkLabel(master=self.frame_acWindow_left_A,
                                                                text="Student Name: ",
                                                                font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_StudentName_label_left.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        # Create the student name entery
        self.ap_stName_entry_left = customtkinter.CTkEntry(master=self.frame_acWindow_left_A,
                                                           border_width=2,
                                                           corner_radius=10,
                                                           width=140)
        self.ap_stName_entry_left.grid(row=1, column=1, pady=10, padx=20, sticky="w")
        self.ap_stName_entry_left.insert(0, "Ex: John Smith, etc...")
        self.ap_stName_entry_left.configure(state="disabled")
        self.ap_stName_entry_left.configure(textvariable=self.stname_Var)
        self.stNameFocus_in = self.ap_stName_entry_left.bind("<Button-1>",
                                                             lambda x: self.on_focus_in(self.ap_stName_entry_left))
        self.stNameFocus_out = self.ap_stName_entry_left.bind("<FocusOut>",
                                                              lambda x: self.on_focus_out(self.ap_stName_entry_left,
                                                                                          "Ex: John Smith, etc..."))

        # Create the student number label
        self.ap_stNo_label_left = customtkinter.CTkLabel(master=self.frame_acWindow_left_A,
                                                         text="Student Number: ",
                                                         font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_stNo_label_left.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        # Create the student number entery
        self.ap_stNo_entry_left = customtkinter.CTkEntry(master=self.frame_acWindow_left_A,
                                                         border_width=2,
                                                         corner_radius=10,
                                                         width=140)
        self.ap_stNo_entry_left.grid(row=2, column=1, pady=10, padx=20, sticky="w")
        self.ap_stNo_entry_left.insert(0, "Ex: s1234567, etc...")
        self.ap_stNo_entry_left.configure(state='disabled')
        self.ap_stNo_entry_left.configure(textvariable=self.stNo_Var)
        self.stNoFocus_in = self.ap_stNo_entry_left.bind("<Button-1>",
                                                         lambda x: self.on_focus_in(self.ap_stNo_entry_left))
        self.stNoFocus_out = self.ap_stNo_entry_left.bind("<FocusOut>",
                                                          lambda x: self.on_focus_out(self.ap_stNo_entry_left,
                                                                                      "Ex: s1234567, etc..."))

        # Create label and entery for the academic year
        self.ap_acadiYear_label_left = customtkinter.CTkLabel(master=self.frame_acWindow_left_A,
                                                              text="Academic Year: ",
                                                              font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_acadiYear_label_left.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        self.ap_acadiYear_Option_left = customtkinter.CTkOptionMenu(master=self.frame_acWindow_left_A,
                                                                    values=["1st Year", "2nd Year", "3rd Year",
                                                                            "3rd plus"],
                                                                    corner_radius=10,
                                                                    width=140,
                                                                    command=self.academicYear_event,
                                                                    variable=self.academicYear_var)
        self.ap_acadiYear_Option_left.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        # Create label and entery for the academic block
        self.ap_acadiBlock_label_left = customtkinter.CTkLabel(master=self.frame_acWindow_left_A,
                                                               text="Academic Block: ",
                                                               font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_acadiBlock_label_left.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        self.ap_acadiBlock_Option_left = customtkinter.CTkOptionMenu(master=self.frame_acWindow_left_A,
                                                                     values=["1st Block", "2nd Block", "3rd Block",
                                                                             "4th Block"],
                                                                     corner_radius=10,
                                                                     width=140,
                                                                     command=self.academicBlock_event,
                                                                     variable=self.academicBlock_var)
        self.ap_acadiBlock_Option_left.grid(row=4, column=1, pady=10, padx=20, sticky="w")

        self.ap_acadiSave_button_left = customtkinter.CTkButton(master=self.frame_acWindow_left_A,
                                                                text="Process",
                                                                command=self.ap_acadiSave_button_left_event)
        self.ap_acadiSave_button_left.grid(row=5, column=0, columnspan=2, pady=10, padx=20, sticky="EW")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frame Left-B ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.frame_acWindow_left_B = customtkinter.CTkFrame(master=self.ap_window, corner_radius=5)
        self.frame_acWindow_left_B.grid(row=2, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="NSEW")
        self.frame_acWindow_left_B.columnconfigure((0, 1), weight=0)
        self.frame_acWindow_left_B.rowconfigure((0, 1, 2, 3, 4), weight=1)
        # Create the frame label
        self.ap_Courses_preferences_label_down = customtkinter.CTkLabel(master=self.frame_acWindow_left_B,
                                                                        text="Courses preferences",
                                                                        font=customtkinter.CTkFont(size=20,
                                                                                                   weight="bold"))  # font name and size in px
        self.ap_Courses_preferences_label_down.grid(row=0, column=0, columnspan=2, pady=5, padx=5, sticky="EW")

        # Faild courses
        self.howManyFailedCoursesLabel = customtkinter.CTkLabel(master=self.frame_acWindow_left_B,
                                                                text="No. of \nFailed Courses: ",
                                                                font=customtkinter.CTkFont(size=14, weight="bold"))
        self.howManyFailedCoursesLabel.grid(row=1, column=0, padx=10, pady=10, sticky="WE")

        self.howManyFailedCoursesEntry = customtkinter.CTkEntry(master=self.frame_acWindow_left_B,
                                                                width=40,
                                                                border_width=2,
                                                                corner_radius=10,
                                                                textvariable=self.howManyFailedCourses_var)
        self.howManyFailedCoursesEntry.grid(row=1, column=1, padx=(50, 10), pady=10, sticky="W")

        # Create label & switch and entery for the 5ec switch
        self.ap_want_5ec_label_down = customtkinter.CTkLabel(master=self.frame_acWindow_left_B,
                                                             text="Wish for extra 5EC: ",
                                                             font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_want_5ec_label_down.grid(row=2, column=0, padx=10, pady=10, sticky="WE")

        self.ap_want_5ec_switch_down = customtkinter.CTkSwitch(master=self.frame_acWindow_left_B,
                                                               text="",
                                                               command=self.doUWant5ectsVar_event,
                                                               onvalue="on",
                                                               offvalue="off",
                                                               variable=self.doWant5ectsVar)
        self.ap_want_5ec_switch_down.grid(row=2, column=1, padx=(50, 10), pady=10, sticky="W")

        # Create a optioMenu button to choose a reason of that 5 EC
        self.ap_5ecReason_label_down = customtkinter.CTkLabel(master=self.frame_acWindow_left_B,
                                                              text="Reason for a 5EC: ",
                                                              font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_5ecReason_label_down.grid(row=3, column=0, padx=10, pady=10, sticky="WE")

        self.ap_5ecReason_Option_down = customtkinter.CTkOptionMenu(master=self.frame_acWindow_left_B,
                                                                    values=["Applying Honours", "Bored",
                                                                            "Quick Graduation", "Catch up"],
                                                                    corner_radius=10,
                                                                    width=140,
                                                                    state="disabled",
                                                                    command=self.ap_5ecReason_Option_down_event,
                                                                    variable=self.reason5ects_var)
        self.ap_5ecReason_Option_down.grid(row=3, column=1, padx=(10, 10), pady=10, sticky="W")

        # Create a label and a switch button to choose if you prefer Englihs or Dutch course
        self.ap_language_label_down = customtkinter.CTkLabel(master=self.frame_acWindow_left_B,
                                                             text="Speaks Dutch: ",
                                                             font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_language_label_down.grid(row=4, column=0, padx=10, pady=10, sticky="WE")

        self.ap_Dutch_switch_down = customtkinter.CTkSwitch(master=self.frame_acWindow_left_B,
                                                            text="",
                                                            font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_Dutch_switch_down.grid(row=4, column=1, padx=(50, 10), pady=10, sticky="W")

        # Create a check box to choose if you took the BSc project's courses already (In case you choose the BSc course)
        self.ap_bscCourses_label_down = customtkinter.CTkLabel(master=self.frame_acWindow_left_B,
                                                               text="First half of the BSc \nproject is compleated:",
                                                               font=customtkinter.CTkFont(size=14, weight="bold"))
        self.ap_bscCourses_label_down.grid(row=5, column=0, padx=10, pady=10, sticky="WE")

        self.ap_bscCourses_switch_down = customtkinter.CTkSwitch(master=self.frame_acWindow_left_B,
                                                                 text="",
                                                                 command=self.followBScProject_event,
                                                                 onvalue="on",
                                                                 offvalue="off",
                                                                 variable=self.followBScProject_var)
        self.ap_bscCourses_switch_down.grid(row=5, column=1, padx=(50, 10), pady=10, sticky="W")

        self.frame_acWindow_right = customtkinter.CTkFrame(master=self.ap_window, width=700, height=850,
                                                           corner_radius=5)
        self.frame_acWindow_right.grid(row=1, column=2, columnspan=3, rowspan=2, padx=(5, 5), pady=(5, 5),
                                       sticky="NSEW")
        self.frame_acWindow_right.columnconfigure((0, 1, 2), weight=0)
        self.frame_acWindow_right.rowconfigure((0, 1), weight=1)

        self.chooseCoursesTab(self.frame_acWindow_right)

        self.grades_button = customtkinter.CTkButton(master=self.frame_acWindow_right,
                                                     text="Add the grades",
                                                     command=self.grading_Window,
                                                     state="disabled")
        self.grades_button.grid(row=1, column=0, padx=10, pady=10, sticky="ws")

        # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ Frame Buttom ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        self.frame_endButtons_Buttom = customtkinter.CTkFrame(master=self.ap_window, corner_radius=5)
        self.frame_endButtons_Buttom.grid(row=3, column=0, columnspan=5, padx=(5, 5), pady=(5, 5), sticky="NSEW")
        self.frame_endButtons_Buttom.columnconfigure((0, 1, 2), weight=1)
        self.frame_endButtons_Buttom.rowconfigure((0, 1, 2), weight=1)
        # create a button to save the user's choices
        self.ap_save_button_right = customtkinter.CTkButton(master=self.frame_endButtons_Buttom,
                                                            text="Advise",
                                                            command=lambda: self.saveButton_event(),
                                                            state="disabled")
        self.ap_save_button_right.grid(row=0, column=0, pady=10, padx=0, sticky="NW")

        # Create a cancle button next to the save one
        self.ap_cancel_button_right = customtkinter.CTkButton(master=self.frame_endButtons_Buttom,
                                                              text="Cancel",
                                                              command=self.unhide_academic_progress_Window_event)
        self.ap_cancel_button_right.grid(row=0, column=0, pady=10, padx=150, sticky="NW")

        # creste a motion of trigging the event based on clicking aroun the canvas
        self.bind_frame_children(self.ap_window)

        self.ap_window.mainloop()

    def bind_frame_children(self, frame):
        for child in frame.winfo_children():
            if isinstance(child, customtkinter.CTkFrame):
                child.bind("<Button-1>", self.leftClick)
                child.bind("<Button-2>", self.middleClick)
                child.bind("<Button-3>", self.rightClick)
                self.bind_frame_children(child)

    # ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
    # ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±± Grading window ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
    # ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
    def grading_Window(self):
        self.grade_window = customtkinter.CTkToplevel(self)
        self.grade_window.geometry(self.get_centered_geometry(self.grade_window, App.HEIGHT, App.WIDTH))
        self.ap_window.withdraw()
        self.grade_window.protocol("WM_DELETE_WINDOW", self.unhide_grading_event)
        self.grade_window.columnconfigure((0, 1, 2), weight=1)
        self.grade_window.resizable(width=True, height=True)  # make window resizable
        self.grade_window.title("Grades")

        # # ++++++++++++++++ frames ++++++++++++++++
        self.grade_windowFrameUp = customtkinter.CTkFrame(master=self.grade_window, corner_radius=5)
        self.grade_windowFrameUp.grid(row=0, column=0, padx=(10, 10), pady=(10, 10), sticky="NSEW")

        self.grade_chosen_courses(self.grade_windowFrameUp)
        for course in self.kb.st.passedCourses:
            if course.title in self.gradeEentries.keys():
                entry = self.gradeEentries[course.title]
                for course2_index in range(len(self.kb.st.passedCourses)):
                    if course.title == self.kb.st.passedCourses[course2_index]:
                        self.kb.st.passedCourses[course2_index].grade = float(entry.get())

        self.grade_windowFrameDown = customtkinter.CTkFrame(master=self.grade_window, corner_radius=5)
        self.grade_windowFrameDown.grid(row=1, column=0, padx=(10, 10), pady=(10, 10), sticky="NSEW")
        # Create a cancle button next to the save one
        self.grade_cancel_button = customtkinter.CTkButton(master=self.grade_windowFrameDown,
                                                           text="Cancel",
                                                           command=self.grade_cancel_button_event)
        self.grade_cancel_button.grid(row=10, column=1, pady=10, padx=5, sticky="sw")

        self.grade_save_button = customtkinter.CTkButton(master=self.grade_windowFrameDown,
                                                         text="Save",
                                                         command=self.grade_save_button_event,
                                                         state="disabled")
        self.grade_save_button.grid(row=10, column=0, pady=10, padx=20, sticky="sw")

    # ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±± Danial's work ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±
    # ±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±±

    # ============ Frame Show the courses that the user has chosen ============
    def grade_chosen_courses(self, frame):
        for var, course in self.check_varsCourses:
            if var.get() == 1:
                if course.title not in [checkCourse.title for checkCourse in self.kb.st.passedCourses]:
                    self.kb.st.passedCourses.append(course)
            else:
                for course2 in self.kb.st.passedCourses:
                    if course2.title == course.title:
                        self.kb.st.passedCourses.remove(course2)
                        break

        entries = []
        for idxCourse, course in enumerate(self.kb.st.passedCourses):
            labelsCheck = customtkinter.CTkLabel(frame, text=course.getTitle(),
                                                 font=customtkinter.CTkFont(size=12, weight="bold"),
                                                 height=30,
                                                 width=240,
                                                 corner_radius=6,  # <- custom corner radius
                                                 fg_color=("white", "gray38")  # <- custom tuple-color
                                                 )
            labelsCheck.grid(row=idxCourse // 3, column=2 * (idxCourse % 3), padx=10, pady=10)

            entryCheck = customtkinter.CTkEntry(master=frame,
                                                border_width=2,
                                                width=40,
                                                corner_radius=10)
            entryCheck.grid(row=idxCourse // 3, column=2 * (idxCourse % 3) + 1, padx=10, pady=10)
            entryCheck.bind("<KeyRelease>",
                            lambda event, entries=entries: self.checkEntry(entries, self.grade_save_button))
            self.gradeEentries[course.getTitle()] = entryCheck

            # Check if a grade was previously entered for this course title and pre-populate the entry
            for passed_course in self.kb.st.passedCourses:
                if passed_course.title == course.title and passed_course.grade != -1:
                    entryCheck.insert(0, str(passed_course.grade))
                    break

    # ============ Frame Show the courses that the user has chosen ============
    def showCourses(self, frame, course_list):
        col = 0
        raww = 1
        for idxCourse, course in enumerate(course_list):
            # print(idxCourse, course.title)
            if not (idxCourse == 0) and idxCourse % 3 == 0:
                raww += 1
                col = 0
            check2 = customtkinter.CTkLabel(frame, text=course.title,
                                            font=customtkinter.CTkFont(size=12, weight="bold"),
                                            # height=30,
                                            # width=240,
                                            corner_radius=6,  # <- custom corner radius
                                            fg_color=("white", "gray38")  # <- custom tuple-color
                                            )
            check2.grid(row=raww, column=col, padx=10, pady=10, sticky="NSEW")
            col += 1

            self.adviced_courses_titel.append(course.title)

    # ====================== Frame Choose the courses ======================
    def chooseCoursesTab(self, frame):
        # Create another tab structure to display the years in each parents tab
        yearTab = customtkinter.CTkTabview(master=frame)
        yearTab.grid(row=0, column=0, columnspan=3, pady=10, padx=20, sticky="NSEW")
        yearTab.grid_columnconfigure(0, weight=0)
        yearTab.grid_rowconfigure(0, weight=0)

        yearTab.add("Year 1")
        yearTab.add("Year 2")
        yearTab.add("Year 3")

        self.makeTabs(yearTab.tab("Year 1"), self.kb.yearOneC)
        self.makeTabs(yearTab.tab("Year 2"), self.kb.yearTwoC)
        self.makeTabs(yearTab.tab("Year 3"), self.kb.yearThreeC)

    def makeTabs(self, frame, year):
        col = 0
        row = 0

        for idxCourse, course in enumerate(year):
            var = tkinter.IntVar()
            self.check_varsCourses.append((var, course))

            check2 = customtkinter.CTkCheckBox(master=frame,
                                               text=course.getTitle(),
                                               font=customtkinter.CTkFont(size=10, weight="bold"),
                                               height=20,
                                               corner_radius=6,  # <- custom corner radius
                                               variable=var,
                                               onvalue=1,
                                               offvalue=0)
            check2.grid(row=row, column=col, padx=10, pady=10, sticky="NSEW")
            if (idxCourse + 1) % 3 == 0:
                row += 1
                col = 0
            else:
                col += 1

    ###############################################################################
    ############################# Utility Functions ##############################
    ###############################################################################

    def get_centered_geometry(self, window, height, width):
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        x_coordinate = (screen_width/2) - (width/2)
        y_coordinate = (screen_height/2) - (height/2)
        return f'{width}x{height}+{int(x_coordinate)}+{int(y_coordinate)}'

    def unhide_academic_progress_Window_event(self):
        self.ap_window.withdraw()
        self.deiconify()

    def unhide_grading_event(self):
        self.grade_window.withdraw()
        self.ap_window.deiconify()

    def change_appearance_mode(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def on_closing(self, event=0):
        self.destroy()

    def instanceCheck(self, widget):
        if isinstance(widget, customtkinter.CTkTextbox):
            widget.delete('1.0', 'end')  # Delete from position 0 till end
        elif isinstance(widget, customtkinter.CTkEntry):
            widget.delete(0, 'end')
        elif isinstance(widget, customtkinter.CTkCheckBox):
            widget.deselect()
        elif isinstance(widget, customtkinter.CTkRadioButton):
            widget.deselect()
        elif isinstance(widget, customtkinter.CTkSwitch):
            widget.deselect()
        elif isinstance(widget, ttk.Treeview):
            widget.delete(*widget.get_children())
        elif isinstance(widget, customtkinter.CTkLabel):
            text = widget.cget("text")
            if text is not None:
                if text == "Name: " + self.kb.st.studentName:
                    widget.configure(text='')
                elif text == "Number: " + str(self.kb.st.studentNumber):
                    widget.configure(text='')
                elif text == "Year: " + self.academicYear_var.get():
                    widget.configure(text='')
                elif text == "Block: " + self.academicBlock_var.get():
                    widget.configure(text='')
                elif text == "Averege: " + str(round(self.kb.st.averageGrade, 2)):
                    widget.configure(text='')
                elif text in self.adviced_courses_titel:
                    widget.destroy()
                else:
                    pass
        else:
            pass

    def reset_widget(self, widget):
        if isinstance(widget, customtkinter.CTkFrame):
            for child in widget.winfo_children():
                self.reset_widget(child)
        else:
            self.instanceCheck(widget)

    def reset_Windows(self, window):
        for child in window.winfo_children():
            if isinstance(child, customtkinter.CTkButton):
                continue
            self.reset_widget(child)

        # Resetting the advises
        if self.kb.ap.recommended_courses:
            if self.frame_recommended_Courses.winfo_exists() == 1:
                self.frame_recommended_Courses.destroy()

        if self.kb.ap.recommended_electives != []:
            if self.frame_elective_courses.winfo_exists() == 1:
                self.frame_elective_courses.destroy()

        if self.kb.ap.showOtherCourses:
            if self.frame_other_courses.winfo_exists() == 1:
                self.frame_other_courses.destroy()

        self.stname_Var = customtkinter.StringVar(0, "Ex: John Smith, etc...")
        self.stNo_Var = customtkinter.StringVar(0, "Ex: s1234567, etc...")
        self.academicBlock_var = customtkinter.StringVar(value="1st Block")
        self.academicYear_var = customtkinter.StringVar(value="1st Year")
        self.doWant5ectsVar = customtkinter.StringVar(value="off")
        self.languageRadio_var = customtkinter.StringVar(value="on")
        self.reason5ects_var = customtkinter.StringVar(value="Choose a reason")
        self.followBScProject_var = customtkinter.StringVar(value="off")
        self.howManyFailedCourses_var = customtkinter.StringVar(0, value="0")
        self.gradeEentries.clear()
        self.check_varsCourses = []

        ###############################################################################

    #################################  Events  ####################################
    ###############################################################################

    def reset_event(self):
        if self.winfo_exists() == 1:
            self.si_Academic_Progress_button_left.configure(state="normal")

        self.reset_Windows(self)

        if hasattr(self, 'ap_window') and self.ap_window.winfo_exists() == 1:
            self.ap_window.destroy()

        if hasattr(self, 'grade_window') and self.grade_window.winfo_exists() == 1:
            self.grade_window.destroy()

        # resetting the classes:
        self.ac = Academic_planning()
        self.kb = Knowledge_Base(Student())
        self.st = self.kb.st

    def stName_event(self):
        if self.stname_Var.get().strip() and self.stNo_Var.get().strip():
            self.kb.st.studentName = self.stname_Var.get()
            self.kb.st.studentNumber = self.stNo_Var.get()
            self.ap_acadiSave_button_left_event()

    def stID_event(self):
        if self.stNo_Var.get().strip() and self.stname_Var.get().strip():
            self.kb.st.studentNumber = self.stNo_Var.get()
            self.kb.st.studentName = self.stname_Var.get()
            self.ap_acadiSave_button_left_event()

    def ap_acadiSave_button_left_event(self):
        stname = self.stname_Var.get()
        stid = self.stNo_Var.get()
        if stname != 'Ex: John Smith, etc...' and stname != '' and stid != 'Ex: s1234567, etc...' and stid != '':
            self.grades_button.configure(state="normal")
        else:
            self.grades_button.configure(state="disabled")

    def on_focus_in(self, entry):
        if entry.cget('state') == 'disabled':
            entry.configure(state='normal')
            entry.delete(0, 'end')
            self.ap_acadiSave_button_left_event()

    def on_focus_out(self, entry, placeholder):
        if entry.get() == "":
            entry.insert(0, placeholder)
            entry.configure(state='disabled')
            self.ap_acadiSave_button_left_event()

    def leftClick(self, event):
        self.on_focus_out(self.ap_stName_entry_left, 'Ex: John Smith, etc...')
        self.on_focus_out(self.ap_stNo_entry_left, 'Ex: s1234567, etc...')
        self.ap_acadiSave_button_left_event()

    def middleClick(self, event):
        self.on_focus_out(self.ap_stName_entry_left, 'Ex: John Smith, etc...')
        self.on_focus_out(self.ap_stNo_entry_left, 'Ex: s1234567, etc...')
        self.ap_acadiSave_button_left_event()

    def rightClick(self, event):
        self.on_focus_out(self.ap_stName_entry_left, 'Ex: John Smith, etc...')
        self.on_focus_out(self.ap_stNo_entry_left, 'Ex: s1234567, etc...')
        self.ap_acadiSave_button_left_event()

    def academicYear_event(self, choice):
        if choice == "1st Year":
            self.kb.st.currentYear = 1
        elif choice == "2nd Year":
            self.kb.st.currentYear = 2
        elif choice == "3rd Year":
            self.kb.st.currentYear = 3
        elif choice == "3rd plus":
            self.kb.st.currentYear = 4

    def academicBlock_event(self, choice):
        if choice == "1st Block":
            self.kb.st.currentBlock = 1
        elif choice == "2nd Block":
            self.kb.st.currentBlock = 2
        elif choice == "3rd Block":
            self.kb.st.currentBlock = 3
        elif choice == "4th Block":
            self.kb.st.currentBlock = 4

    def doUWant5ectsVar_event(self):
        if self.doWant5ectsVar.get() == 'on':
            self.kb.st.want5ECTS = True
            self.ap_5ecReason_Option_down.configure(state="normal")
        else:
            self.kb.st.want5ECTS = False
            self.ap_5ecReason_Option_down.configure(state="disabled")

    def ap_5ecReason_Option_down_event(self, choice):
        self.kb.st.reason5ECTS = choice

    def languageRadio_event(self):
        if self.languageRadio_var.get() == 'English':
            self.kb.st.language = True
        else:
            self.kb.st.language = False

    def followBScProject_event(self):
        if self.followBScProject_var.get() == 'on':
            self.kb.st.startedBachelorProject = True
        else:
            self.kb.st.startedBachelorProject = False

    # related to the tree panel
    def courseGrade_inserting_event(self):
        for course in self.kb.st.passedCourses:
            self.gradingTree.insert("", "end", values=(course.title, course.grade))

    def infoBoxName_event(self):
        self.pr_SInfoName_label_left.configure(text="Name: " + self.kb.st.studentName)

    def infoBoxNumber_event(self):
        self.pr_SInfoNumber_label_left.configure(text="Number: " + self.kb.st.studentNumber)

    def infoBoxYear_event(self):
        self.pr_SInfoYear_label_left.configure(text="Year: " + self.academicYear_var.get())

    def infoBoxBlock_event(self):
        self.pr_SInfoBlock_label_left.configure(text="Block: " + self.academicBlock_var.get())

    def infoBoxAverage_event(self):
        self.pr_SInfoAverageGrade_label_left.configure(text="Averege: " + str(round(self.kb.st.averageGrade, 2)))

    def grade_save_button_event(self):
        self.ap_save_button_right.configure(state='normal')
        for course in self.kb.st.passedCourses:
            if course.title in self.gradeEentries.keys():
                entry = self.gradeEentries[course.title]
                course.grade = float(entry.get())

                # Update the value in the gradeEentries dictionary
                self.gradeEentries[course.title].delete(0, 'end')
                self.gradeEentries[course.title].insert(0, str(course.grade))
        self.unhide_grading_event()

    def grade_cancel_button_event(self):
        self.grade_window.withdraw()
        self.ap_window.deiconify()

    # this function goes through the list again to check that the courses are all in passed courses with a grade
    def makePassedList(self):
        for course in self.kb.st.passedCourses:
            if course.title in self.gradeEentries.keys():
                entry = self.gradeEentries[course.title]
                for course2_index in range(len(self.kb.st.passedCourses)):
                    if course.title == self.kb.st.passedCourses[course2_index].title:
                        self.kb.st.passedCourses[course2_index].grade = float(entry.get())

    ### This function does inference plus extra things
    def runInference(self):
        # copy current year from student to academic planning
        self.kb.ap.planYear = self.kb.st.currentYear
        self.kb.ap.planBlock = self.kb.st.currentBlock
        # make sure that the courses in the allcourses list also have the grades from passedCourses
        for course in self.kb.courses.allcourses:
            for course2 in self.kb.st.passedCourses:
                if course.title == course2.title:
                    course.grade = course2.grade
        # the dbCourses.py has pre requisites as course name strings instead of course objects
        # this transforms it into course objects
        self.kb.courses.convertToCourses()
        self.kb.courses.getAllYears()
        # calculate average grade
        if len(self.kb.st.passedCourses) == 0:
            self.kb.st.averageGrade = 0
        else:
            self.kb.st.averageGrade = sum([course.grade for course in self.kb.st.passedCourses]) / len(
                self.kb.st.passedCourses)

        # reset the all years because they did not have the grades yet
        self.kb.courList = self.kb.courses.getAllcourses()
        self.kb.yearOneC = self.kb.courses.yearOneCour
        self.kb.yearTwoC = self.kb.courses.yearTwoCour
        self.kb.yearThreeC = self.kb.courses.yearThreeCour
        # actuall do the inference
        self.kb.doInference()

    # def grade_save_button_event(self):
    #     self.ap_save_button_right.configure(state="normal")
    #     self.unhide_grading_event()

    def checkEntry(self, entries, button_widget):
        # if entry_widget.get() == "":
        #     button_widget.configure(state="disabled")
        # else:
        #     button_widget.configure(state="normal")
        for entry in entries:
            if entry.get() == "":
                button_widget.configure(state="disabled")
                return
        button_widget.configure(state="normal")

    def saveButton_event(self):

        # if you did not select the dropdown menu it stays at none so set it one because its the default value.
        if (self.kb.st.currentYear == None):
            self.kb.st.currentYear = 1
        if (self.kb.st.currentBlock == None):
            self.kb.st.currentBlock = 1

        # go through the list again to make sure the passed courses are all in there with the grades
        self.makePassedList()
        self.kb.st.failedCourses = self.howManyFailedCourses_var.get()
        # do the inference in this function with some extra transformations
        self.runInference()

        self.stName_event()
        self.stID_event()

        if self.kb.ap.recommended_courses != []:
                # --------- frame_advise in frame_right ---------
            self.frame_advise = customtkinter.CTkFrame(master=self.frame_right, corner_radius=10)
            self.frame_advise.grid(row=1, column=0, pady=5, padx=5, sticky="NSWE")
            self.frame_advise.columnconfigure(1, weight=1)
            self.frame_advise.rowconfigure(1, weight=5)

            self.ad_advise_label_right = customtkinter.CTkLabel(master=self.frame_advise,
                                                                text="Advise",
                                                                font=customtkinter.CTkFont(size=20,
                                                                                        weight="bold"))  # font name and size in px
            self.ad_advise_label_right.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="WE")
        ### Make three frames. One for each output list from the inference in the knowledge base
        # first the recommended courses
            self.frame_recommended_Courses = customtkinter.CTkFrame(master=self.frame_advise, width=240, corner_radius=10)
            self.frame_recommended_Courses.grid(row=1, column=0, columnspan=2, rowspan=10, pady=20, padx=20, sticky="NSWE")

            recommended_courses = []
            for course in self.kb.ap.recommended_courses:
                if course not in self.kb.st.passedCourses:
                    recommended_courses.append(course)

            self.kb.ap.recommended_courses = recommended_courses
            self.showCourses(self.frame_recommended_Courses, self.kb.ap.recommended_courses)
            
        # second if its not empty the recommended electives with the same orientation and practicals
        if self.kb.ap.recommended_electives != []:
            # --------- frame_Prograss in frame_right ---------

            self.frame_elective = customtkinter.CTkFrame(master=self.frame_right, corner_radius=10)
            self.frame_elective.grid(row=2, column=0, pady=5, padx=5, sticky="NSWE")

            self.frame_elective_label_right = customtkinter.CTkLabel(master=self.frame_elective,
                                                                     text="Elective courses",
                                                                     font=customtkinter.CTkFont(size=20,
                                                                                                weight="bold"))  # font name and size in px
            self.frame_elective_label_right.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky="WE")
            self.frame_right.rowconfigure(2, weight=5)  # set weight of third row to be 5
            self.frame_elective.grid_columnconfigure(0, weight=1)
            self.frame_elective.grid_rowconfigure(1, weight=1)

            self.frame_elective_courses = customtkinter.CTkFrame(master=self.frame_elective, width=240,
                                                                 corner_radius=10)
            self.frame_elective_courses.grid(row=1, column=0, columnspan=2, rowspan=10, pady=20, padx=20, sticky="NSWE")

            self.showCourses(self.frame_elective_courses, self.kb.ap.recommended_electives)

        # third the electives with a different orientation if there are not enough electives with the same orientation
        if self.kb.ap.showOtherCourses:
            # --------- frame_OtherCourses in frame_right ---------
            self.frame_OtherCourses = customtkinter.CTkFrame(master=self.frame_right, corner_radius=10)
            self.frame_OtherCourses.grid(row=3, column=0, pady=5, padx=5, sticky="NSWE")
            self.frame_right.rowconfigure(3, weight=5)  # set weight of third row to be 5
            self.frame_OtherCourses.grid_columnconfigure(0, weight=1)
            self.frame_OtherCourses.grid_rowconfigure(1, weight=1)

            self.pr_otherCourses_label_right = customtkinter.CTkLabel(master=self.frame_OtherCourses,
                                                                      text="Other courses",
                                                                      font=customtkinter.CTkFont(size=20,
                                                                                                 weight="bold"))  # font name and size in px
            self.pr_otherCourses_label_right.grid(row=0, column=0, columnspan=2, pady=5, padx=10, sticky="WE")

            self.frame_other_courses = customtkinter.CTkFrame(master=self.frame_OtherCourses, width=240,
                                                              corner_radius=10)
            self.frame_other_courses.grid(row=1, column=0, columnspan=2, rowspan=10, pady=20, padx=20, sticky="NSWE")

            self.showCourses(self.frame_other_courses, self.kb.ap.other_available_electives)

        if self.kb.st.reason5ECTS == "Applying Honours" or self.kb.st.reason5ECTS == "Bored" or self.kb.st.reason5ECTS == "Quick Graduation":
            self.pr_textExplanation_textBox_down.insert(tkinter.END,
                                                        text="This is a valid reason to pursue an extra 5EC. Therefore, you get extra recommendations to choose from.\n For further inquiries, we encourage you to contact the student advisor for a legitimate advice.\n")
        else:
            self.pr_textExplanation_textBox_down.insert(tkinter.END,
                                                        text="A valid reason would be Applying for Honours or being motivated. Hence this is not a valid reason.\n Therefore, you get extra recommendations to choose from. For further inquiries, we encourage you to contact the student advisor for a legitimate advice\n")
        self.courseGrade_inserting_event()
        self.infoBoxName_event()
        self.infoBoxNumber_event()
        self.infoBoxYear_event()
        self.infoBoxBlock_event()

        self.infoBoxAverage_event()
        self.unhide_academic_progress_Window_event()
