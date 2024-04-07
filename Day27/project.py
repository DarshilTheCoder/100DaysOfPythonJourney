#Day27 Project Miles to Km converter 
from tkinter import *

tk = Tk()
tk.title("Miles to KM Converter")
tk.minsize(width=300,height=270)
tk.config(padx=20,pady=20)

def convert():
    miles_input = float(mile_input_box.get())
    km = miles_input*1.60934
    km_answer.config(text=f"{km}")

mile_input_box = Entry(width=20)
mile_input_box.grid(row=0,column=1)

mile_label = Label(text="Miles")
mile_label.grid(row=0,column=2)

is_equal_to = Label(text='is equal to ')
is_equal_to.grid(row=1,column=0)
is_equal_to.config(padx=10,pady=10)

km_answer = Label(text='0')
km_answer.grid(row=1,column=1)
km_answer.config(padx=10,pady=10)

km_label = Label(text="Miles")
km_label.grid(row=1,column=2)
km_label.config(padx=10,pady=10)

button =Button(text="Calculate",command=convert)
button.grid(row=2,column=1)








tk.mainloop()