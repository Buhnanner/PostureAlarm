"""
Kipland Melton
A program to notify you of your bad posture

Mac Build .35M

Whats new:

    time entry and save, implemented in full effect mac version

PZ Software
May 23, 2020
"""

# Graphics based UI library
from tkinter import *
# Image manipulation with pillow
from PIL import Image, ImageTk
# Time library for alarm function
from time import sleep

window_X = 270
window_Y = 80

"""
Home page can be referred to as page one, options page two, etc..
Could be smarter to create an algorithm for keep up with page structure on the fly instead
of hard coding in back buttons on every page.. just a thought



Simply add a counter that is increased/decreased based on which pages are chosen?

Start : Page 1
> Clicks options
>> Page 2
>>> Clicks back, page = 1
>>>> Clicks forward, page = 2 
"""


class Main_Window:

    def __init__(self, master):

        self.page = 1
        
        self.master = master
        self.frame = Frame(self.master)

        self.master.title("PostureAlarm")

        self.b1 = Button(self.master, text="Exit", width=3, fg='black',command=master.quit)
        self.b2 = Button(self.master, text="+", width=3, bg='#433e46',command=self.options_navigation)

        self.info_text = Label(self.master, text='Sit Up Buddy!')
        self.info_text.pack()

        self.b1.place(x=70,y=20)
        self.b2.place(x=130,y=20)

        self.frame.pack()

    def options_navigation(self):
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
        self.forward_button.place(x=20,y=0)

        self.frame.pack()

        self.master.wm_iconbitmap('officechair.icns') # Declares icon for options window

        self.timeEntrySave = StringVar()
        self.Alarm_entry = Entry(self.master, width=4, textvariable=self.timeEntrySave)
        self.Alarm_entry.place(x=100, y=23)  # Creates text box for time entry
        self.submit_time = Button(self.master, text='Submit',command=self.TimeEntry_ToFile)
        self.submit_time.place(x=85,y=50)

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
    backbutton = r"/Users/kipland/Documents/Python/PostureAlarm/Images/arrow-left.png"
    forwardbutton = r"/Users/kipland/Documents/Python/PostureAlarm/Images/arrow-right.png"

    # Image packing and resizing
    back_image = Image.open(backbutton)
    forward_image = Image.open(forwardbutton)
    back_image = back_image.resize((12,12), Image.ANTIALIAS)
    forward_image = forward_image.resize((12,12), Image.ANTIALIAS)

    # Final images
    back_image_resize = ImageTk.PhotoImage(back_image)
    forward_image_resize = ImageTk.PhotoImage(forward_image)




    ###################
    # Root properties #
    ###################
    MainWindow = Main_Window(root)
    root.minsize(window_X,window_Y)


    root.geometry("+1670+960")  #+1670+1000 for noti window
    root.wm_iconbitmap('officechair.icns')
    root.mainloop()


