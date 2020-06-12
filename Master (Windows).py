"""
Kipland Melton
A program to notify you of your bad posture

Windows Build .27W

PZ Software
May 23, 2020
"""

# Graphics based UI library
from tkinter import *
# Image manipulation with pillow
from PIL import Image, ImageTk
# Time library for alarm function
from time import sleep

window_X = 240
window_Y = 50

class Main_Window:

    def __init__(self, master):

        self.page = 1

        self.master = master
        self.frame = Frame(self.master)

        self.master.title("PostureAlarm")

        self.b1 = Button(self.master, text="Close", width=4, command=master.quit)
        self.b2 = Button(self.master, text="+", width=4,command=self.new_window)

        self.info_text = Label(self.master, text='Sit Up Buddy!')
        self.info_text.pack()

        self.b1.place(x=80,y=20)
        self.b2.place(x=120,y=20)

        self.frame.pack()

    def new_window(self):
        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Opt_activate = Options_Window(self.newWindow)
        self.newWindow.minsize(window_X,window_Y)
        self.newWindow.geometry("+1670+960")
        self.page += 1
        print(self.page)



class Options_Window():     # Classifies the alternate options menu

    def __init__(self, master):
        self.master = master
        self.frame = Frame(self.master)

        self.options_text = Label(self.master, text="Set Alert Interval (Minutes)") # Window Description
        self.options_text.pack()

        self.back_button = Button(self.master, image=back_image_resize, command=self.back_button) # Back Button
        self.forward_button = Button(self.master, image=forward_image_resize) # Forward Button
        self.back_button.place(x=0,y=0)
        self.forward_button.place(x=17,y=0)

        self.frame.pack()

        self.master.wm_iconbitmap('officechair.ico') # Declares icon for options window

        # the placement of the submit button/time entry is not good, reposition PLEASE
        self.timeEntrySave = StringVar()
        self.Alarm_entry = Entry(self.master, width=4, textvariable=self.timeEntrySave)
        self.Alarm_entry.place(x=90, y=23)  # Creates text box for time entry
        self.submit_time = Button(self.master, text='Submit',command=self.TimeEntry_ToFile)
        self.submit_time.place(x=110,y=23)

    def TimeEntry_ToFile(self):
        usertime = self.Alarm_entry.get()
        with open('time_entry.txt', 'a') as file_object:
            file_object.write(usertime) 


    def back_button(self):

        self.master.withdraw()
        self.newWindow = Toplevel(self.master)
        Opt_activate = Main_Window(self.newWindow)
        self.newWindow.minsize(window_X,window_Y)
        self.newWindow.geometry("+1670+960")
        self.page -= 1



if __name__ == '__main__':
    root = Tk()
    
    # File path for back/forward buttons
    backbutton = r"C:\Users\kip_m\Desktop\Python\PostureAlarm\Images\arrow-left.png"
    forwardbutton = r"C:\Users\kip_m\Desktop\Python\PostureAlarm\Images\arrow-right.png"

    # Image packing and resizing
    back_image = Image.open(backbutton)
    forward_image = Image.open(forwardbutton)
    back_image = back_image.resize((16,16), Image.ANTIALIAS)
    forward_image = forward_image.resize((16,16), Image.ANTIALIAS)

    # Final images
    back_image_resize = ImageTk.PhotoImage(back_image)
    forward_image_resize = ImageTk.PhotoImage(forward_image)


    ###################
    # Root properties #
    ###################
    MainWindow = Main_Window(root)
    root.minsize(window_X,window_Y)

    root.geometry("+1670+960")  #+1670+1000 for noti window
    root.wm_iconbitmap('officechair.ico')
    root.mainloop()