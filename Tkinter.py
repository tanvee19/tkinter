# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 22:51:38 2019

@author: Tanvee
"""
import tkinter

window = tkinter.Tk()
# to rename the title of the window
window.title("GUI")
# pack is used to show the object in the window
label = tkinter.Label(window, text = "Hello World!").pack()


# creating 2 frames TOP and BOTTOM
top_frame = tkinter.Frame(window).pack()
bottom_frame = tkinter.Frame(window).pack(side = "bottom")

# now, create some widgets in the top_frame and bottom_frame
btn1 = tkinter.Button(top_frame, text = "Button1", fg = "red").pack(side = "right")
# 'fg - foreground' is used to color the contents
btn2 = tkinter.Button(top_frame, text = "Button2", fg = "green").pack()
# 'text' is used to write the text on the Button
btn3 = tkinter.Button(bottom_frame, text = "Button3", fg = "purple").pack()
# 'side' is used to align the widgets
btn4 = tkinter.Button(bottom_frame, text = "Button4", fg = "orange").pack(side = "left")


# creating 3 simple Labels containing any text

# sufficient width
tkinter.Label(window, text = "Suf. width", fg = "white", bg = "purple").pack()

# width of X
tkinter.Label(window, text = "Taking all available X width", fg = "white", bg = "green").pack(fill = "x")

# height of Y
tkinter.Label(window, text = "Taking all available Y height", fg = "white", bg = "black").pack(side = "left", fill = "y")

# creating 2 text labels and input labels

tkinter.Label(window, text = "Username").grid(row = 0) # this is placed in 0 0
# 'Entry' is used to display the input-field
tkinter.Entry(window).grid(row = 0, column = 1) # this is placed in 0 1

tkinter.Label(window, text = "Password").grid(row = 1) # this is placed in 1 0
tkinter.Entry(window).grid(row = 1, column = 1) # this is placed in 1 1

# 'Checkbutton' is used to create the check buttons
tkinter.Checkbutton(window, text = "Keep Me Logged In").grid(columnspan = 2) 
# 'columnspan' tells to take the width of 2 columns
# you can also use 'rowspan' in the similar manner



# creating a function called say_hi()
def say_hi():
    tkinter.Label(window, text = "Hi").pack()

tkinter.Button(window, text = "Click Me!", command = say_hi).pack() 
# 'command' is executed when you click the button

# creating a function with an arguments 'event'
def say_hi(event): # you can rename 'event' to anything you want
    tkinter.Label(window, text = "Hi").pack()

btn = tkinter.Button(window, text = "Click Me!")
btn.bind("<Button-1>", say_hi)
# 'bind' takes 2 parameters 1st is 'event' 2nd is 'function'
btn.pack()

#creating 3 different functions for 3 events
def left_click(event):
    tkinter.Label(window, text = "Left Click!").pack()

def middle_click(event):
    tkinter.Label(window, text = "Middle Click!").pack()

def right_click(event):
    tkinter.Label(window, text = "Right Click!").pack()

window.bind("<Button-1>", left_click)
window.bind("<Button-2>", middle_click)
window.bind("<Button-3>", right_click)

class GeeksBro:

    def __init__(self, window):

        self.text_btn = tkinter.Button(window, text = "Click Me!", command = self.say_hi) 
        # create a button to call a function called 'say_hi'
        self.text_btn.pack()

        self.close_btn = tkinter.Button(window, text = "Close", command = window.quit)
        # closing the 'window' when you click the button
        self.close_btn.pack()

    def say_hi(self):
        tkinter.Label(window, text = "Hi").pack()

window = tkinter.Tk()
window.title("GUI")

geeks_bro = GeeksBro(window)

def function():
    pass

# creating a root menu to insert all the sub menus
root_menu = tkinter.Menu(window)
window.config(menu = root_menu)

# creating sub menus in the root menu
file_menu = tkinter.Menu(root_menu)
 # it intializes a new sub menu in the root menu
root_menu.add_cascade(label = "File", menu = file_menu)
 # it creates the name of the sub menu
file_menu.add_command(label = "New file.....", command = function) 
# it adds a option to the sub menu 'command' parameter is used to do some action
file_menu.add_command(label = "Open files", command = function)
file_menu.add_separator() 
# it adds a line after the 'Open files' option
file_menu.add_command(label = "Exit", command = window.quit)

# creting another sub menu
edit_menu = tkinter.Menu(root_menu)
root_menu.add_cascade(label = "Edit", menu = edit_menu)
edit_menu.add_command(label = "Undo", command = function)
edit_menu.add_command(label = "Redo", command = function)

import tkinter.messagebox
# creating a simple alert box
tkinter.messagebox.showinfo("Alert Message", "This is just a alert message!")
# creating a question to get the response from the user [Yes or No Question]
response = tkinter.messagebox.askquestion("Simple Question", "Do you love Python?")
# If user clicks 'Yes' then it returns 1 else it returns 0
if response == 1:
    tkinter.Label(window, text = "You love Python!").pack()
else:
    tkinter.Label(window, text = "You don't love Python!").pack()
    

# creating the 'Canvas' area of width and height 500px
canvas = tkinter.Canvas(window, width = 500, height = 500)
canvas.pack()

# 'create_line' is used to create a line. Parameters:- (starting x-point, starting y-point, ending x-point, ending y-point)
line1 = canvas.create_line(25, 25, 250, 150)
# parameter:- (fill = color_name)
line2 = canvas.create_line(25, 250, 250, 150, fill = "red")

# 'create_rectangle' is used to create rectangle. Parameters:- (starting x-point, starting y-point, width, height, fill)
# starting point the coordinates of top-left point of rectangle
rect = canvas.create_rectangle(500, 25, 175, 75, fill = "green")

# you 'delete' shapes using delete method passing the name of the variable as parameter.
canvas.delete(line1)
# you 'delete' all the shapes by passing 'ALL' as parameter to the 'delete' method
# canvas.delete(tkinter.ALL)

# taking image from the directory and storing the source in a variable
icon = tkinter.PhotoImage(file = "forsk-logo.png")
# displaying the picture using a 'Label' by passing the 'picture' variriable to 'image' parameter
label = tkinter.Label(window, image = icon)
label.pack()

                                                             
window.mainloop()
