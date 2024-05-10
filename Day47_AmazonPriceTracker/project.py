import requests,smtplib,os
from bs4 import BeautifulSoup
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()
headers = {
    'Accept-Language':'en-US,en;q=0.7',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
}
response = requests.get('https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5XW6TN/ref=sr_1_1_sspa?crid=2Y3HBONCTB8SE&dib=eyJ2IjoiMSJ9.4P8mgIyS6Wf0zGUUhDJvzb8bjzWmJH1hpb_lIwX96hLctmeNw3wU1hQLzpBwr5JAJrCQIMBvSt1wfur2ttn2QpcUCcGlnGEudQFH5FsdHVUXmN2JJlDwOpmsn1psLP6-oh1ppyEIuZfcHAP4YxGoYpQjpQu-Y_9ThPo_8QMBN6-XguqUOEZSiLG2LvQqiRNhXOnzFG4KcEdJHQc7WoEsBZsdr_JYOmtZ8fKo0eAOmLQ.FWffVryhjMDo5AKTwFx2pltyqbnFPyKpX1KY0A5S92w&dib_tag=se&keywords=samsung+s24+ultra+5g&qid=1715315866&sprefix=sam%2Caps%2C199&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1',headers=headers)

amazon_website = response.text
soup = BeautifulSoup(amazon_website,'html.parser')
title = soup.title.get_text().split(':')[0]
print(title)
price_tag = soup.find(name='span',class_ ='a-price-whole')
price = round(float(price_tag.get_text().replace(',','')),2)
print(price)
# print(type(price_float))
if price < 150000:
    server_host = "smtp.gmail.com"
    server_port = os.getenv('server_port')

    # #Setup Gmail credentials
    my_email = os.getenv('email_id')
    my_password = os.getenv('app_password')

    # #Sender and receiver email
    sender = os.getenv('email_id')
    receiver = os.getenv('sender_id')

        # #Setup Subject and to,from
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = 'Amazon Price Alert'
            
    #setup body 
    body = str(f'{title}\n Now Price of the Product is {price}\n https://www.amazon.in/Samsung-Galaxy-Smartphone-Titanium-Storage/dp/B0CS5XW6TN/ref=sr_1_1_sspa?crid=2Y3HBONCTB8SE&dib=eyJ2IjoiMSJ9.4P8mgIyS6Wf0zGUUhDJvzb8bjzWmJH1hpb_lIwX96hLctmeNw3wU1hQLzpBwr5JAJrCQIMBvSt1wfur2ttn2QpcUCcGlnGEudQFH5FsdHVUXmN2JJlDwOpmsn1psLP6-oh1ppyEIuZfcHAP4YxGoYpQjpQu-Y_9ThPo_8QMBN6-XguqUOEZSiLG2LvQqiRNhXOnzFG4KcEdJHQc7WoEsBZsdr_JYOmtZ8fKo0eAOmLQ.FWffVryhjMDo5AKTwFx2pltyqbnFPyKpX1KY0A5S92w&dib_tag=se&keywords=samsung+s24+ultra+5g&qid=1715315866&sprefix=sam%2Caps%2C199&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1')
    msg.attach(MIMEText(body,'plain'))
            
    with smtplib.SMTP(server_host,server_port) as server_connection:
        server_connection.starttls()
        server_connection.login(user=my_email,password=my_password)
        text = msg.as_string()
        server_connection.sendmail(from_addr=sender,to_addrs=receiver,msg=text)

