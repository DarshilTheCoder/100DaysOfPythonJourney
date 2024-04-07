from tkinter import * 
from generatepassword import generatePassword
from addData import addData
from searchFile import Search

FONT_NAME="Arial"


# ---------------------------- FIND PASSWORD------------------------------- #
def find_password():
    website_name =website_input.get()
    search = Search(website_name)
    search.find_password()


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    passwordgenerator = generatePassword()
    password = passwordgenerator.generatepassword()
    password_input.insert(0,password)
    
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_data():
    website_name = website_input.get()
    username_email = email_username_input.get()
    password = password_input.get()
    addDataToFile = addData(website_name,username_email,password)
    addDataToFile.addData()
    
    website_input.delete(0,END)
    password_input.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

windows = Tk()
windows.title("Password Generator")
windows.config(padx=50,pady=50)


canvas = Canvas(width=200,height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=lock_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website: ",foreground="black",font=(FONT_NAME,10,"bold"))
website_label.grid(row=2,column=0)

website_input = Entry(width=25)
website_input.grid(row=2,column=1)
website_input.focus()

search_button = Button(text="Search",font=(FONT_NAME,10,"bold"),foreground='black',command=find_password)
search_button.grid(row=2,column=2)

email_username_label = Label(text="Email/Username: ",foreground="black",font=(FONT_NAME,10,"bold"))
email_username_label.grid(row=4,column=0)

email_username_input = Entry(width=38)
email_username_input.grid(row=4,column=1,columnspan=2)
email_username_input.insert(0,"darshil@gmail.com")

password_input_label = Label(text="Password: ",foreground="black",font=(FONT_NAME,10,"bold"))
password_input_label.grid(row=6,column=0)

password_input = Entry(width=25)
password_input.grid(row=6,column=1)

password_generator = Button(text="Generate",foreground="black",font=(FONT_NAME,10,"bold"),command=generate_password)
password_generator.grid(row=6,column=2)

add_button = Button(text="Add",foreground="black",font=(FONT_NAME,10,"bold"),width=35,command=add_data)
add_button.grid(row=8,column=1,columnspan=2)
windows.mainloop()