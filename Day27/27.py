#Day27 Learning about tkinter, which is used to create a GUI for computer, also heard the story of first GUI computer named as MAC Lisa

from tkinter import *

windows = Tk()
windows.title("My First GUI Program")
windows.minsize(width=500,height=300)
FONT = ('Arial',25,'italic')

#Creating a Label
my_label = Label(text='I am a Label',font=FONT)
my_label.pack()

my_label['text'] = 'New Text'
# my_label.config(text = 'Another New Text')

#Creating Buttons
def button_clicked():
    # print('I got clicked')
    input_value = input.get()
    my_label['text'] = input_value

button = Button(text='Click Me',command=button_clicked)
button.pack()

#Creating input field
input= Entry(width=50,foreground='black',textvariable='enter here')

input.pack()
windows.mainloop()