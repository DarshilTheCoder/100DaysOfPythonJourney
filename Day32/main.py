import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#Setup SMTP Serer 
smtp_server= "smtp.gmail.com"
smtp_port = 587

#My gmail Credentials
my_email = "darshil.20becev124@gmail.com"
my_password = ""
my_password2 = "" #for darshil.coder350@gmail.com

#Sender and Receiver Email Address
receiver = "darshil.coder350@gmail.com"
sender = "darshil.20becev124@gmail.com"

#Creating Message Container
# msg = MIMEMultipart()
# msg['From'] = sender
# msg['To'] = receiver
# msg['Subject'] = "Test Email"

#Creating Body of email
# body = "This is the first email using python"
# msg.attach(MIMEText(body,"plain"))


#Creating connection
connection = smtplib.SMTP(smtp_server,smtp_port)
connection.starttls() #TLS means transport Layer Security it wll encrypt our email msg 
connection.login(user=my_email,password=my_password)
# text = msg.as_string()
connection.sendmail(from_addr=sender,to_addrs= receiver,msg="Subject:Hello2 \n\n This is second test python mail")
connection.close()
