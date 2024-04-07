import json
from tkinter import messagebox

class Search:
    def __init__(self,website_name):
        self.website = website_name
        
    def find_password(self):
        try:
            with open('jsonData.json',mode='r') as jsonFile:
                self.data = json.load(jsonFile)
        except FileNotFoundError:
            messagebox.showerror(title='Error',message="No file is found")
        else:
            if self.website in self.data:
                messagebox.showinfo(title="Search",message=f"Email:{self.data[self.website]['email']} \n Password:{self.data[self.website]['password']}")
            else:
                messagebox.showerror(title='Error',message=f"No such data is exist for {self.website}")
