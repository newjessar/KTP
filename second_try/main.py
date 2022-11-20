from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

def reset_action(root,frame):
    frame.destroy()
    frame_start_screen(root,frame)
    
def start_action(root,frame):
    frame.destroy()
    frame_passed_courses_mandatory(root,frame)
    
def quit_action(root,frame):
    root.destroy()
    
def elective_action(root,frame):
    frame.destroy()
    frame_start_screen(root,frame)
    
def frame_passed_courses_mandatory(root,frame):
    frame = Frame(root)
    frame.pack()
    
    button_frame = Frame(frame)
    text_frame = Frame(frame)
    
    button_frame.grid(row=0,column=0)
    text_frame.grid(row=1,column=0)
    
    reset_button = Button(button_frame,text= "Reset",command=lambda: reset_action(root,frame))
    elective_button = Button(button_frame,text= "CONTINUE",command=lambda: elective_action(root,frame))
    empty_label = Label(button_frame,text="         ")
    quit_button = Button(button_frame,text= "Quit",command=lambda: quit_action(root,frame))
    label = Label(text_frame,text="Select Mandatory Courses Passed")
    
    reset_button.grid(row=0,column=0)
    quit_button.grid(row=0,column=3)
    empty_label.grid(row=0,column=2)
    elective_button.grid(row=0,column=1)
    label.grid(row=0,column=0,padx=10,pady=10)
    
    select_frame = Frame(text_frame)
    select_frame.grid(row=1,column=0)
    
    year1_frame = Frame(select_frame,width=300,height=400)
    year2_frame = Frame(select_frame,width=300,height=400)
    year3_frame = Frame(select_frame,width=300,height=400)
    
    year1_frame.grid(row=0,column=0,padx=10,pady=10,stick=N)
    year1_label = Label(year1_frame,text="year 1")
    year1_label.grid(row=0,column=0)
    year1_courses_frame = Frame(year1_frame)
    year1_courses_frame.grid(row=1,column=0)
    
    
    year2_frame.grid(row=0,column=1,padx=10,pady=10,stick=N)
    year2_label = Label(year2_frame,text="year 2")
    year2_label.grid(row=0,column=0)
    year2_courses_frame = Frame(year2_frame)
    year2_courses_frame.grid(row=1,column=0)
    
    year3_frame.grid(row=0,column=2,padx=10,pady=10,stick=N)
    year3_label = Label(year3_frame,text="year 3")
    year3_label.grid(row=0,column=0)
    year3_courses_frame = Frame(year3_frame)
    year3_courses_frame.grid(row=1,column=0)
    
    year1_frame.grid_propagate(0)
    year2_frame.grid_propagate(0)
    year3_frame.grid_propagate(0)
    
    Yr1Block1a_frame = Frame(year1_courses_frame)
    Yr1Block1b_frame = Frame(year1_courses_frame)
    Yr1Block2a_frame = Frame(year1_courses_frame)
    Yr1Block2b_frame = Frame(year1_courses_frame)
    
    Yr1Block1a_frame.grid(row=0,column=0,stick=W)
    Yr1Block1b_frame.grid(row=1,column=0,stick=W)
    Yr1Block2a_frame.grid(row=2,column=0,stick=W)
    Yr1Block2b_frame.grid(row=3,column=0,stick=W)
    
    Yr2Block1a_frame = Frame(year2_courses_frame)
    Yr2Block1b_frame = Frame(year2_courses_frame)
    Yr2Block2a_frame = Frame(year2_courses_frame)
    Yr2Block2b_frame = Frame(year2_courses_frame)
    
    Yr2Block1a_frame.grid(row=0,column=0,stick=W)
    Yr2Block1b_frame.grid(row=1,column=0,stick=W)
    Yr2Block2a_frame.grid(row=2,column=0,stick=W)
    Yr2Block2b_frame.grid(row=3,column=0,stick=W)
    
    Yr3Block1a_frame = Frame(year3_courses_frame)
    Yr3Block1b_frame = Frame(year3_courses_frame)
    Yr3Block2a_frame = Frame(year3_courses_frame)
    Yr3Block2b_frame = Frame(year3_courses_frame)
    
    Yr3Block1a_frame.grid(row=0,column=0,stick=W)
    Yr3Block1b_frame.grid(row=1,column=0,stick=W)
    Yr3Block2a_frame.grid(row=2,column=0,stick=W)
    Yr3Block2b_frame.grid(row=3,column=0,stick=W)
    
    Yr1Block1a_label = Label(Yr1Block1a_frame,text="1a")
    Yr1Block1b_label = Label(Yr1Block1b_frame,text="1b")
    Yr1Block2a_label = Label(Yr1Block2a_frame,text="2a")
    Yr1Block2b_label = Label(Yr1Block2b_frame,text="2b")  
    
    Yr2Block1a_label = Label(Yr2Block1a_frame,text="1a")
    Yr2Block1b_label = Label(Yr2Block1b_frame,text="1b")
    Yr2Block2a_label = Label(Yr2Block2a_frame,text="2a")
    Yr2Block2b_label = Label(Yr2Block2b_frame,text="2b")   
    
    Yr3Block1a_label = Label(Yr3Block1a_frame,text="1a")
    Yr3Block1b_label = Label(Yr3Block1b_frame,text="1b")
    Yr3Block2a_label = Label(Yr3Block2a_frame,text="2a")
    Yr3Block2b_label = Label(Yr3Block2b_frame,text="2b")   
    
    Yr1Block1a_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr1Block1b_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr1Block2a_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr1Block2b_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    
    Yr2Block1a_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr2Block1b_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr2Block2a_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr2Block2b_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    
    Yr3Block1a_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr3Block1b_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr3Block2a_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    Yr3Block2b_label.grid(row=0,column=0,padx=10,pady=10,stick=W+N)
    
    Yr1Block1a = ["introduction to AI"]
    Yr1Block1b = ["basic scientific skills"]
    Yr1Block2a = ["cognitive psychology"]
    Yr1Block2b = ["linear algebra and multivariable calculus"]
    
    Yr2Block1a = ["language and speech technology","statistics (for AI)","knowledge and agent technology"]
    Yr2Block1b = ["a","b"]
    Yr2Block2a = ["a","b"]
    Yr2Block2b = ["a","b"]
    
    Yr3Block1a = ["Artificial intelligence 2"]
    Yr3Block1b = ["a","b"]
    Yr3Block2a = ["a","b"]
    Yr3Block2b = ["a","b"]
    
    coursesYr1 = [Yr1Block1a,Yr1Block1b,Yr1Block2a,Yr1Block2b]
    coursesYr2 = [Yr2Block1a,Yr2Block1b,Yr2Block2a,Yr2Block2b]
    coursesYr3 = [Yr3Block1a,Yr3Block1b,Yr3Block2a,Yr3Block2b]
    coursesAll = [coursesYr1,coursesYr2,coursesYr3]
    courseVar = {}
    
    
    
    for year in coursesAll:
        for block in year:
            for course in block:
                courseVar[course] = StringVar()
    cb = {}  
    frameList = [[Yr1Block1a_frame,Yr1Block1b_frame,Yr1Block2a_frame,Yr1Block2b_frame],[Yr2Block1a_frame,Yr2Block1b_frame,Yr2Block2a_frame,Yr2Block2b_frame],\
        [Yr3Block1a_frame,Yr3Block1b_frame,Yr3Block2a_frame,Yr3Block2b_frame]]
    
    for year in range(len(coursesAll)):
        for block in range(len(coursesAll[year])):
            for courseNumber in range(len(coursesAll[year][block])):
                course = coursesAll[year][block][courseNumber]
                block_frame = frameList[year][block]
                cb[course] = Checkbutton(block_frame,text=course,variable=courseVar[course],onvalue=course,offvalue="off")
                cb[course].grid(row=courseNumber+1,column=0,stick=W+N)
                


def frame_start_screen(root,frame):
    frame = Frame(root)
    frame.pack()
    
    button_frame = Frame(frame)
    text_frame = Frame(frame)
    
    button_frame.grid(row=0,column=0)
    text_frame.grid(row=1,column=0)
    
    start_button = Button(button_frame,text= "START",command=lambda: start_action(root,frame))
    quit_button = Button(button_frame,text= "QUIT",command=lambda: quit_action(root,frame))
    label = Label(text_frame,text="Press start to begin choosing a course")
    
    start_button.grid(row=0,column=0)
    quit_button.grid(row=0,column=1)
    label.grid(row=0,column=0)

def main():
    root = Tk()
    root.title('Course Selection for dummies')
    root.geometry("1200x800")
    
    frame = Frame(root)
    frame.pack()
    
    button_frame = Frame(frame)
    text_frame = Frame(frame)
    
    button_frame.grid(row=0,column=0)
    text_frame.grid(row=1,column=0)
    
    start_button = Button(button_frame,text= "START",command=lambda: start_action(root,frame))
    quit_button = Button(button_frame,text= "QUIT",command=lambda: quit_action(root,frame))
    label = Label(text_frame,text="Press start to begin choosing a course")
    
    start_button.grid(row=0,column=0)
    quit_button.grid(row=0,column=1)
    label.grid(row=0,column=0)
    
    root.mainloop()



if __name__ == "__main__":
    main()