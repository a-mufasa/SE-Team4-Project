from tkinter import *


def splash_screen():
    
    #make it a toplevel screen
    splash_root = Toplevel()
    splash_root.title("Splash Screen")
    splash_root.geometry("800x800")                                 #dimensions of splash screen. 
    splash_root.overrideredirect(True)                              #gets rid of boarders, looks cleaner
    splash_image = PhotoImage(file="test_image4.png")               #image to be displayed, name can be changed to whatever path needed
    splash_lable = Label(master = splash_root, image = splash_image)#setting up label to show the image
    splash_lable.pack()                                             #packing the label
    splash_root.after(3000, splash_root.destroy)                    #wait 3000ms and then destroy itself
    splash_root.mainloop()                                          #mainloop because tkinter
    return 0                                                        #return zero



if __name__ == '__main__':
    
    #a "main" screen to call the function from.
    root = Tk()
    root.title("Test Program")
    root.geometry("800x800")
    my_button = Button(root, text="test call",command=splash_screen)
    my_button.pack(pady=20)
    root.mainloop()