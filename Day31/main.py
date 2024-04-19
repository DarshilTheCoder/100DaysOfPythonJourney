from tkinter import *
import pandas as pd
import random as rd
BACKGROUND_COLOR = "#B1DDC6"
current_word = {}


#CREATE NEW FLASH CARD
try:
    read_data = pd.read_csv('./data/words_to_learn.csv')
except FileNotFoundError:
    read_data = pd.read_csv('./data/french_words.csv')
    list_of_dict = read_data.to_dict(orient='records')
else:
    list_of_dict = read_data.to_dict(orient="records")

def create_new_flash_card():
    global current_word,flip_timer
    flip_timer = windows.after_cancel(flip_timer)
    current_word = rd.choice(list_of_dict)
    print(current_word)
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text= current_word["French"],fill="black")
    canvas.itemconfig(old_image,image=front_card_img)
    flip_timer= windows.after(3000,func=flip_flash_card)

#Save data to words_to_learn.csv   
def is_known():
    list_of_dict.remove(current_word)
    data = pd.DataFrame(list_of_dict)
    data.to_csv('./data/words_to_learn.csv',index=False)
    
    create_new_flash_card()
    
    
#FLIP THE FLASHC CARD
def flip_flash_card():
    global current_word
    canvas.itemconfig(card_title,text="English",fill="white")
    canvas.itemconfig(card_word,text=current_word["English"],fill="white")
    canvas.itemconfig(old_image,image=back_card_img)
    
    
    
#CREATE UI 

windows = Tk()
windows.title("Flashy")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
flip_timer = windows.after(3000,flip_flash_card)

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
front_card_img = PhotoImage(file='./images/card_front.png')
back_card_img = PhotoImage(file='./images/card_back.png')
old_image = canvas.create_image(400,263,image=front_card_img)
card_title = canvas.create_text(400,150,text="",font=('Ariel',40,'italic')) #the coordinate positions are relative to canvas 
card_word = canvas.create_text(400,263,text="",font=('Ariel',60,'bold')) 
canvas.grid(row=0,column=0,columnspan=2)
create_new_flash_card()

unknown_img = PhotoImage(file='./images/wrong.png')
unknown_btn = Button(image=unknown_img,highlightthickness=0,command=create_new_flash_card)
unknown_btn.grid(row=1,column=0)

known_img = PhotoImage(file='./images/right.png')
known_btn = Button(image=known_img,highlightthickness=0,command=is_known)
known_btn.grid(row=1,column=1)



windows.mainloop()

#SAVE THE PROGRESS
