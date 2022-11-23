from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
import tkinter.ttk as ttk

def reset_action(root,frame):
    frame.destroy()
    frame_start_screen(root)
    
def start_action(root,frame):
    frame.destroy()
    frame_passed_courses_mandatory(root)
    
def quit_action(root,frame):
    root.destroy()
    
def elective_action(root,frame):
    frame.destroy()
    frame_start_screen(root)
    
def able_start(root):
    global start_button
    global chosen_year
    global chosen_block
    if (chosen_year.get()=="" or chosen_block.get()==""):
        return
    else:
        start_button.configure(state=NORMAL)
        return

def frame_passed_courses_mandatory(root):
    frame = Frame(root)
    frame.configure(bg=default_color)
    frame.pack(padx=20,pady=20)
 
    button_frame = Frame(frame,bg=default_color)
    text_frame = Frame(frame,bg=default_color)
    
    button_frame.grid(row=0,column=0)
    text_frame.grid(row=1,column=0)
    
    reset_button = Button(button_frame,text= "Reset",command=lambda: reset_action(root,frame))
    elective_button = Button(button_frame,text= "CONTINUE",command=lambda: elective_action(root,frame))
    empty_label = Label(button_frame,text="         ",bg=default_color)
    quit_button = Button(button_frame,text= "Quit",command=lambda: quit_action(root,frame))
    label = Label(text_frame,text="Select Mandatory Courses Passed",bg=default_color)
    
    reset_button.grid(row=0,column=0)
    quit_button.grid(row=0,column=3)
    empty_label.grid(row=0,column=2)
    elective_button.grid(row=0,column=1)
    label.grid(row=0,column=0,padx=10,pady=10)
    
    select_frame = Frame(text_frame,bg=default_color)
    select_frame.grid(row=1,column=0)
    
    year1_frame = Frame(select_frame,width=300,height=400,bg=default_color)
    year2_frame = Frame(select_frame,width=300,height=400,bg=default_color)
    year3_frame = Frame(select_frame,width=300,height=400,bg=default_color)
    
    year1_frame.grid(row=0,column=0,padx=10,pady=10,stick=N)
    year1_label = Label(year1_frame,text="year 1",bg=default_color)
    year1_label.grid(row=0,column=0)
    year1_courses_frame = Frame(year1_frame,bg=default_color)
    year1_courses_frame.grid(row=1,column=0)
    
    
    year2_frame.grid(row=0,column=1,padx=10,pady=10,stick=N)
    year2_label = Label(year2_frame,text="year 2",bg=default_color)
    year2_label.grid(row=0,column=0)
    year2_courses_frame = Frame(year2_frame,bg=default_color)
    year2_courses_frame.grid(row=1,column=0)
    
    year3_frame.grid(row=0,column=2,padx=10,pady=10,stick=N)
    year3_label = Label(year3_frame,text="year 3",bg=default_color)
    year3_label.grid(row=0,column=0)
    year3_courses_frame = Frame(year3_frame,bg=default_color)
    year3_courses_frame.grid(row=1,column=0)
    
    year1_frame.grid_propagate(0)
    year2_frame.grid_propagate(0)
    year3_frame.grid_propagate(0)
    
    Yr1Block1a_frame = Frame(year1_courses_frame,bg=default_color)
    Yr1Block1b_frame = Frame(year1_courses_frame,bg=default_color)
    Yr1Block2a_frame = Frame(year1_courses_frame,bg=default_color)
    Yr1Block2b_frame = Frame(year1_courses_frame,bg=default_color)
    
    Yr1Block1a_frame.grid(row=0,column=0,stick=W)
    Yr1Block1b_frame.grid(row=1,column=0,stick=W)
    Yr1Block2a_frame.grid(row=2,column=0,stick=W)
    Yr1Block2b_frame.grid(row=3,column=0,stick=W)
    
    Yr2Block1a_frame = Frame(year2_courses_frame,bg=default_color)
    Yr2Block1b_frame = Frame(year2_courses_frame,bg=default_color)
    Yr2Block2a_frame = Frame(year2_courses_frame,bg=default_color)
    Yr2Block2b_frame = Frame(year2_courses_frame,bg=default_color)
    
    Yr2Block1a_frame.grid(row=0,column=0,stick=W)
    Yr2Block1b_frame.grid(row=1,column=0,stick=W)
    Yr2Block2a_frame.grid(row=2,column=0,stick=W)
    Yr2Block2b_frame.grid(row=3,column=0,stick=W)
    
    Yr3Block1a_frame = Frame(year3_courses_frame,bg=default_color)
    Yr3Block1b_frame = Frame(year3_courses_frame,bg=default_color)
    Yr3Block2a_frame = Frame(year3_courses_frame,bg=default_color)
    Yr3Block2b_frame = Frame(year3_courses_frame,bg=default_color)
    
    Yr3Block1a_frame.grid(row=0,column=0,stick=W)
    Yr3Block1b_frame.grid(row=1,column=0,stick=W)
    Yr3Block2a_frame.grid(row=2,column=0,stick=W)
    Yr3Block2b_frame.grid(row=3,column=0,stick=W)
    
    Yr1Block1a_label = Label(Yr1Block1a_frame,text="1a",bg=default_color)
    Yr1Block1b_label = Label(Yr1Block1b_frame,text="1b",bg=default_color)
    Yr1Block2a_label = Label(Yr1Block2a_frame,text="2a",bg=default_color)
    Yr1Block2b_label = Label(Yr1Block2b_frame,text="2b",bg=default_color)  
    
    Yr2Block1a_label = Label(Yr2Block1a_frame,text="1a",bg=default_color)
    Yr2Block1b_label = Label(Yr2Block1b_frame,text="1b",bg=default_color)
    Yr2Block2a_label = Label(Yr2Block2a_frame,text="2a",bg=default_color)
    Yr2Block2b_label = Label(Yr2Block2b_frame,text="2b",bg=default_color)   
    
    Yr3Block1a_label = Label(Yr3Block1a_frame,text="1a",bg=default_color)
    Yr3Block1b_label = Label(Yr3Block1b_frame,text="1b",bg=default_color)
    Yr3Block2a_label = Label(Yr3Block2a_frame,text="2a",bg=default_color)
    Yr3Block2b_label = Label(Yr3Block2b_frame,text="2b",bg=default_color)   
    
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
    Yr2Block2a = ["c","d"]
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
                cb[course] = Checkbutton(block_frame,text=course,variable=courseVar[course],onvalue=course,offvalue="off",bg=default_color)
                cb[course].grid(row=courseNumber+1,column=0,stick=W+N)
                


def frame_start_screen(root):
    frame = Frame(root)
    global default_color
    frame.configure(bg=default_color)
    frame.pack(padx=20,pady=20)
    
    button_frame = Frame(frame)
    text_frame = Frame(frame)
    option_year_frame = Frame(frame)
    option_block_frame = Frame(frame)

    button_frame.grid(row=1,column=2)
    option_year_frame.grid(row=1,column=0)
    option_block_frame.grid(row=1,column=1)
    text_frame.grid(row=0,column=0,columnspan=3)
    text_frame.configure(bg=default_color)
    option_block_frame.configure(bg=default_color)
    option_year_frame.configure(bg=default_color)

    title_frame = Frame(text_frame)
    title_frame.configure(bg=default_color)
    genText_frame = LabelFrame(text_frame)
    genText_frame.configure(bg=default_color)
    title_frame.grid(row=0,column=0)
    genText_frame.grid(row=1,column=0,padx=10,pady=10,ipadx=10,ipady=10)
    
    global start_button
    start_button = Button(button_frame,text= "START",command=lambda: start_action(root,frame),state=DISABLED)
    quit_button = Button(button_frame,text= "QUIT",command=lambda: quit_action(root,frame))
    title_label = Label(title_frame,text="Starting Page",font=("Arial", 25))
    title_label.configure(bg=default_color)
    genText_label = Label(genText_frame,text="This application helps you in determining the courses to select for your AI bachelor program.\
        First select the year you are in and for which block you want to select courses to follow and then press start.")
    genText_label.configure(bg=default_color)
    start_button.grid(row=0,column=0)
    quit_button.grid(row=0,column=1)
    title_label.grid(row=0,column=0)
    genText_label.grid(row=0,column=0)
    
    global chosen_year
    global chosen_block
    chosen_year = StringVar()
    chosen_block = StringVar()
    chosen_year.set("")
    chosen_block.set("")
    year_MODES = [
        ("year 1","year1"),
        ("year 2","year2"),
        ("year 3","year3"),
        ("year 4+","year4+")
    ]

    block_MODES = [
        ("block 1a","block1a"),
        ("block 1b","block1b"),
        ("block 2a","block2a"),
        ("block 2b","block2b")
    ]

    year_label = Label(option_year_frame,text="choose year you are in",font=("Arial", 15))
    block_label = Label(option_block_frame,text = "choose block to schedule",font=("Arial", 15))
    year_label.grid(row=0,column=0)
    year_label.configure(bg=default_color)   
    block_label.configure(bg=default_color)   
    block_label.grid(row=0,column=0)

    rb = {}
    for mode in range(len(year_MODES)):
        rb[year_MODES[mode][1]] =  Radiobutton(option_year_frame,text=year_MODES[mode][0],\
            variable=chosen_year,value=year_MODES[mode][1],bg=default_color,command=lambda: able_start(root)).grid(row=mode+1,column=0,stick=W)
        #rb[year_MODES[mode][1]].configure(bg=default_color)    

    for mode in range(len(year_MODES)):
        rb[block_MODES[mode][1]] = Radiobutton(option_block_frame,text=block_MODES[mode][0],\
            variable=chosen_block,value=block_MODES[mode][1],bg=default_color,command=lambda: able_start(root)).grid(row=mode+1,column=0,stick=W)
        #rb[block_MODES[mode][1]].configure(bg=default_color)



def main():
    root = Tk()
    global default_color
    default_color = "white"
    root.configure(bg=default_color)
    root.title('Course Selection for dummies')
    root.geometry("1200x800")
    
    frame_start_screen(root)

    root.mainloop()



if __name__ == "__main__":
    main()