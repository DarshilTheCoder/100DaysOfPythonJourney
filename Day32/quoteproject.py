import smtplib, datetime as dt ,random as rd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText



#Setup Server config
server_host = "smtp.gmail.com"
server_port = 587

# #Setup Gmail credentials
my_email = "darshil.coder350@gmail.com"
my_password = ""

# #Sender and receiver email
sender = "darshil.coder350@gmail.com"
receiver = "darshil.200410107017@gmail.com"

# #Setup Subject and to,from
msg = MIMEMultipart()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = "Motivational Quotes"

#Setup body 
with open('quotes.txt',mode='r') as quotesFile:
    quotesList = list(quotesFile)
    # print(quotesList)
body = str(rd.choice(quotesList))
msg.attach(MIMEText(body,'plain'))
# print(body)
# print(type(body))

#Setup connection
now = dt.datetime.now()
today_day =now.weekday()
if today_day == 2:
    with smtplib.SMTP(server_host,server_port) as server_connection:
        server_connection.starttls()
        server_connection.login(user=my_email,password=my_password)
        text = msg.as_string()
        server_connection.sendmail(from_addr=sender,to_addrs=receiver,msg=text)
