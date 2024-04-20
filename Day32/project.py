##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes. 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
import smtplib, datetime as dt ,random as rd,pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

PLACEHOLDER = "[NAME]"
now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month,today_day)
# print(today)

birthdayFile = pd.read_csv('birthdays.csv')
dict = birthdayFile.to_dict(orient="records")
birthday_dict = {(data_row.month,data_row.day):data_row for (index,data_row) in birthdayFile.iterrows()}
if today in birthday_dict:
    birthday_person = birthday_dict[today]
    letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
    random_letter= rd.choice(letters)
    with open(f'./letter_templates/{random_letter}',mode='r') as letter:
            letter_content = letter.read()
            new_letter = letter_content.replace(PLACEHOLDER,birthday_person['Name'])
            # Setup Server config
            server_host = "smtp.gmail.com"
            server_port = 587

            # #Setup Gmail credentials
            my_email = "darshil.coder350@gmail.com"
            my_password = "your password"

            # #Sender and receiver email
            sender = "darshil.coder350@gmail.com"
            receiver = birthday_person['email']

            # #Setup Subject and to,from
            msg = MIMEMultipart()
            msg['From'] = sender
            msg['To'] = receiver
            msg['Subject'] = "Birthday Wishes🎂🥳"
            
            #setup body 
            body = str(new_letter)
            msg.attach(MIMEText(body,'plain'))
            
            with smtplib.SMTP(server_host,server_port) as server_connection:
                server_connection.starttls()
                server_connection.login(user=my_email,password=my_password)
                text = msg.as_string()
                server_connection.sendmail(from_addr=sender,to_addrs=receiver,msg=text)
# for person in dict:
#     if today == (person['month'],person['day']):
#         name = person['Name']
#         letters = ['letter_1.txt','letter_2.txt','letter_3.txt']
#         random_letter= rd.choice(letters)
#         with open(f'./letter_templates/{random_letter}',mode='r') as letter:
#             letter_content = letter.read()
#             new_letter = letter_content.replace(PLACEHOLDER,name)
#             #Setup Server config
#             server_host = "smtp.gmail.com"
#             server_port = 587

#             # #Setup Gmail credentials
#             my_email = "darshil.coder350@gmail.com"
#             my_password = "werc vutc xdxz wrkv"

#             # #Sender and receiver email
#             sender = "darshil.coder350@gmail.com"
#             receiver = person['email']

#             # #Setup Subject and to,from
#             msg = MIMEMultipart()
#             msg['From'] = sender
#             msg['To'] = receiver
#             msg['Subject'] = "Birthday Wishes🎂🥳"
            
#             #setup body 
#             body = str(new_letter)
#             msg.attach(MIMEText(body,'plain'))
            
#             with smtplib.SMTP(server_host,server_port) as server_connection:
#                 server_connection.starttls()
#                 server_connection.login(user=my_email,password=my_password)
#                 text = msg.as_string()
#                 server_connection.sendmail(from_addr=sender,to_addrs=receiver,msg=text)

