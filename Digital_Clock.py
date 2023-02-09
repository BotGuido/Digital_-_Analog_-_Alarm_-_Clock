from tkinter import *
from tkinter.ttk import *
'''
The strftime () method in the time module takes one or more format codes 
as an argument and returns a formatted string based on it. 
This function is used to retrieve the time of the particular system.
'''
from time import strftime
root = Tk()
root.title('Digital Clock')
'''
Function time is used to retrieve the time from the respective system and display the time in the window
'''
def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text = string)
    lbl.after(1000, time)
lbl = Label(root, font = ('franklin gothic', 40, 'bold'),
            background = 'black',
            foreground = 'white')
lbl.pack(anchor = 'center')
time()
mainloop()