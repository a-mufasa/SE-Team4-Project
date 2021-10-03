from tkinter import *


def splash_screen():
    
    #make it a toplevel screen
    splash_root = Toplevel()
    splash_root.title("Splash Screen")
    
    #gets rid of the window boarders
    splash_root.overrideredirect(True)
        
    #pull image to be shown and label/pack into screen
    splash_image = PhotoImage(file="splash_logo.png")
    
    #pull size info from image
    winWidth = splash_image.width()
    winHeight = splash_image.height()
    
    #label and pack image to screen
    splash_lable = Label(master = splash_root, image = splash_image)
    splash_lable.pack()
    
    #some stuff to make it open in the upper middle of the screen
    x = int(splash_root.winfo_screenwidth()/2 - winWidth/2)
    y = int(splash_root.winfo_screenheight()/3 - winHeight/2)
    splash_root.geometry(f'{winWidth}x{winHeight}+{x}+{y}') 
    
    #wait 3000ms and destroy self
    splash_root.after(3000, splash_root.destroy)
    splash_root.mainloop()
    
    #return 0
    return 0                   

'''
#Test main and function call
if __name__ == '__main__':
    
    #a "main" screen to call the function from.
    root = Tk()
    root.title("Test Program")
    root.geometry("800x800")
    my_button = Button(root, text="test call",command=splash_screen)
    my_button.pack(pady=20)
    root.mainloop()
'''
