from tkinter import *
from tkinter import messagebox
import json

class addData:
    def __init__(self,website_name,username_email,password):
        self.website = website_name
        self.username = username_email
        self.password = password
        self.new_dict = {
            self.website:
                {
            "email": self.username,
            "password":self.password
        }
    }
    
    def addData(self):
        if self.website =="" or self.password=="":
            messagebox.showinfo(title="Oops",message="Please don't leave any field empty")
        else:
            is_ok = messagebox.askokcancel(title=self.website,message=f"These are details entered :\n Email: {self.username}\n Password:{self.password}")
            
            if is_ok:
                # with open('datafile.txt',mode='a') as data:
                    # data.write(f"{self.website} | {self.username} | {self.password} \n")
                try:
                    with open('jsonData.json',mode='r') as jsonFile:
                        #Reading data from json file 
                        data = json.load(jsonFile)
                except FileNotFoundError:
                    with open('jsonData.json',mode='w') as jsonFile:
                        json.dump(self.new_dict,jsonFile,indent=4)
                else:
                    #Updating data in json file
                    data.update(self.new_dict)
                    with open('jsonData.json',mode='w') as jsonFile:
                        json.dump(data,jsonFile,indent=4)
                
    