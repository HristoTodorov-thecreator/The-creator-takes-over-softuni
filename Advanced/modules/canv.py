
from tkinter import Tk,Canvas

def create_root():
    window = Tk()

    window.geometry('700x600') # the size of the program
    window.title('Gui Shop') # title for the program

    window.resizable(False,False) # blocking the resize of the program

    return window


def create_frame():
    frame = Canvas(window,width=700,height=700) # we create the frame( grafic )
    frame.grid(row=0,column=0) # place it at the window row 0 col 0

    return frame


window = create_root()
frame = create_frame()

