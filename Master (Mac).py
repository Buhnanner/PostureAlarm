"""
Kipland Melton
A program to notify you of your bad posture

11/30/2019
"""
# Graphics based UI library
from tkinter import *
# Image manipulation with pillow
from PIL import Image
# Time library for alarm function
from time import sleep

window_X = 240
window_Y = 50


"""
wTaskbar_posX = 1670
wTaskbar_posY = 960
"""


class Main_Window:

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("PostureAlarm")

        self.b1 = Button(self.master, text="Close", width=4, command=master.quit)
        self.b2 = Button(self.master, text="+", width=4,command=self.new_window)

        self.info_text = Label(self.master, text='Sit Up!')
        self.info_text.pack()

        self.b1.place(x=60,y=20)
        self.b2.place(x=120,y=20)

        self.back_button = Button(self.master, image=backbutton,  height=16, width = 16) # Back Button
        self.forward_button = Button(self.master, image=forwardbutton, height=16, width = 16) # Forward Button
        self.back_button.place(x=0,y=0)
        self.forward_button.place(x=40,y=0)

        self.frame.pack()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Opt_activate = Options_Window(self.newWindow)
        self.newWindow.minsize(window_X,window_Y)
        self.newWindow.geometry("+1670+960")





class Options_Window():     # Classifies the alternate options menu

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.options_text = Label(self.master, text="Set Alert Interval (Minutes)") # Window Description
        self.options_text.pack()

        Minute = 60 # Minute is to be multiplied by whichever number the user enters
        User_Time = StringVar()

        self.back_button = Button(self.master, image=backbutton) # Back Button
        self.forward_button = Button(self.master, image=forwardbutton) # Forward Button
        self.back_button.place(x=0,y=0)
        self.forward_button.place(x=17,y=0)

        self.frame.pack()

        self.master.wm_iconbitmap('officechair.ico') # Declares icon for options window

        self.Alarm_entry = Entry(self.master, width=4, textvariable=User_Time).place(x=100, y=23)  # Creates text box for time entry



if __name__ == '__main__':
    root = Tk()

    # Couldn't recognize the data in image file?
    # > For some reason tkinter doesnt want to accept any file type besides .gif , not jpg or png.
    backbutton = PhotoImage(file=r'/Users/kipland/Documents/Python/PostureAlarm/Images/arrow-left.gif')
    forwardbutton = PhotoImage(file=r'/Users/kipland/Documents/Python/PostureAlarm/Images/arrow-right.gif')


    MainWindow = Main_Window(root)
    root.minsize(window_X,window_Y)


    root.geometry("+1670+960")  #+1670+1000 for noti window
    root.wm_iconbitmap('officechair.ico')
    root.mainloop()


