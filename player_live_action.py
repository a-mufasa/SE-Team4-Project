from tkinter import *
from tkinter import font
import tkinter
from tkinter.font import Font
#from udp_socket import get_recent_hits_action()

all_red_labels = []     #Complete render list for red window
all_green_labels = []   #Complete render list for green window 
font_size = 15
sub_frame_height = 10

def red_action(window, height, width, arr, frame=None):
    global all_red_labels
    sub_frame_height = Font(font=('Helvetica',font_size)).metrics('linespace')+5
    #Main frame creation
    if frame == None:
        frame = Frame(window, width=width, height=height, bg='black')
    #Creating various sub frames containing the labels of players who shot and got shot
    for tuple in arr:
        sub_frame=Frame(frame, width=width, height=sub_frame_height, bg='black')
        shooter_label=Label(sub_frame, text=tuple[0], fg = 'red', bg='black',font=('Helvetica', font_size))
        hit_label = Label(sub_frame, text='hit', fg = 'white', bg='black',font=('Helvetica', font_size))
        shot_label=Label(sub_frame, text=tuple[1], fg = 'green', bg='black',font=('Helvetica', font_size))
        shooter_label.grid(row=0,column=0,sticky='w')
        hit_label.grid(row=0,column=1,sticky='w')
        shot_label.grid(row=0,column=2,sticky='w')
        all_red_labels.append(sub_frame)    #adding to render list
    j=0
    #Outputting the labels in render list (red)
    for sub_frame in reversed(all_red_labels):
        tmp = height-j*sub_frame_height
        if tmp > 0:
            sub_frame.pack()
            sub_frame.place(x=50, y=tmp, anchor='sw')
        else:
            sub_frame.destroy()
            frame.update()
        j+=1
    return frame

def green_action(window, height, width, arr, frame=None):
    global all_green_labels
    sub_frame_height = Font(font=('Helvetica',font_size)).metrics('linespace')+5
    #Main frame creation
    if frame == None:
        frame = Frame(window, width=width, height=height, bg='black')
    #Creating various sub frames containing the labels of players who shot and got shot
    for tuple in arr:
        sub_frame=Frame(frame, width=width, height=sub_frame_height, bg='black')
        shooter_label=Label(sub_frame, text=tuple[0], fg = 'green', bg='black',font=('Helvetica', font_size))
        hit_label = Label(sub_frame, text='hit', fg = 'white', bg='black',font=('Helvetica', font_size))
        shot_label=Label(sub_frame, text=tuple[1], fg = 'red', bg='black',font=('Helvetica', font_size))
        shooter_label.grid(row=0,column=0,sticky='w')
        hit_label.grid(row=0,column=1,sticky='w')
        shot_label.grid(row=0,column=2,sticky='w')
        all_green_labels.append(sub_frame)    #adding to render list
    j=0
    #Outputting the labels in render list
    for sub_frame in reversed(all_green_labels):
        tmp = height-j*sub_frame_height
        if tmp > 0:
            sub_frame.pack()
            sub_frame.place(x=width-50, y=tmp, anchor='se')
        else:
            sub_frame.destroy()
            frame.update()
        j+=1
    return frame