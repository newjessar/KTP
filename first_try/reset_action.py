from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

def reset(frame,root):
    from frame_start_screen import Frame_start_screen
    frame.destroy()
    Frame_start_screen(root)