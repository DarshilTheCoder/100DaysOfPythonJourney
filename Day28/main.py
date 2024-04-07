from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    windows.after_cancel(timer)
    canvas.itemconfig(timer_text,text = "25:00")
    timer_label.config(text='Timer')
    check_marks.config(text="")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    if reps == 8:
        timer_label.config(text="LONG BREAK")
        count_down(long_break_sec)
    elif reps%2 != 0 :
        timer_label.config(text="WORK TIME")
        count_down(work_sec)
    elif reps%2 == 0:
        timer_label.config(text="SHORT BREAK")
        count_down(short_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_minutes = math.floor(count/60)
    count_seconds = (count%60)
    #this is called a Dynamic Typing
    #where you check count_sec in int and then change it to string 
    if count_seconds <10:
        count_seconds = f"0{count_seconds}"
    canvas.itemconfig(timer_text,text=f"{count_minutes}:{count_seconds}")
    if count>0:
        global timer
        timer = windows.after(1000,count_down,count-1)
    else:
        reps+=1
        mark = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            mark+="✔️"
        check_marks.config(text=mark)
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
windows = Tk()
windows.title("Pomodaro Timer")
windows.config(padx=100,pady=100,bg=YELLOW)

timer_label = Label(text="Timer",foreground=GREEN,font=(FONT_NAME,30,"bold"),background=YELLOW,highlightthickness=0)
timer_label.grid(row=0,column=2)

canvas = Canvas(width=200,height=224,background=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,20,"bold"))
canvas.grid(row=1,column=2)

start_button = Button(text="Start",highlightthickness=0,font=(FONT_NAME,10,"bold"),command=start_timer)
start_button.grid(row=2,column=0)

check_marks = Label(text="",foreground=GREEN,background=YELLOW,font=(FONT_NAME,20,"bold"))
check_marks.grid(row=2,column=2)

reset_button = Button(text="Reset",highlightthickness=0,font=(FONT_NAME,10,"bold"),command=reset_timer)
reset_button.grid(row=2,column=3)


windows.mainloop()