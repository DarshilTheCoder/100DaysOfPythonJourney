import os , requests
from datetime import datetime,timedelta
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv() #used to load the env files

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

today_date = datetime.now().date()
yesterday_date = today_date - timedelta(days=1)
day_before_yesterday_date = today_date - timedelta(days=2)
today_day = today_date.weekday()
yesterday_day = yesterday_date.weekday()
day_before_yesterday_day = day_before_yesterday_date.weekday()

parameters = {
    'function':'TIME_SERIES_DAILY',
    'symbol':STOCK,
    'apikey' : os.getenv('STOCK_API_KEY')
    # 'apikey' : 'R2B0TX8JPTJ8VN8M'
}
news_parameters = {
    'q':COMPANY_NAME,
    'from': yesterday_date,
    'sortBy':'popularity',
    'apiKey': os.getenv('NEWS_API_KEY')
}
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

account_sid = os.getenv('sid')
auth_token = os.getenv('token')
client = Client(account_sid, auth_token)

def getting_stock_data(parameters, STOCK_ENDPOINT):
    response = requests.get(url=STOCK_ENDPOINT,params=parameters)
    response.raise_for_status()
    return response.json()
def getting_news_data(news_parameters, NEWS_ENDPOINT):
    news_response = requests.get(url=NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    articles = news_response.json()['articles']
    return articles
def formatted_articles(three_articles):
    return [f"Heading : {articles['title']}\n Brief:{articles['description']}" for articles in three_articles]


if today_day ==5 or today_day==6:
    print('Stock Market is CLOSED !! Please come on Monday to buy or sell stocks')
else:
    if today_day == 0 or today_day == 1:
        yesterday_date = today_date - timedelta(days=3)
        day_before_yesterday_date = today_date - timedelta(days=4)
    data = getting_stock_data(parameters = parameters, STOCK_ENDPOINT = STOCK_ENDPOINT)
    yesterday_stock_price = float(data["Time Series (Daily)"][str(yesterday_date)]['4. close'])
    day_before_yesterday_stock_price = float(data["Time Series (Daily)"][str(day_before_yesterday_date)]['4. close']) 


    percentage_change = round(((yesterday_stock_price - day_before_yesterday_stock_price) / day_before_yesterday_stock_price)* 100,0)
    print(percentage_change)
    up_down = None
    if percentage_change > 0:
        up_down = "🔼"
    else:
        up_down = "🔽"
        

    if abs(percentage_change)>=5:
        articles = getting_news_data(news_parameters = news_parameters, NEWS_ENDPOINT = NEWS_ENDPOINT)
        three_articles = articles[:3]
        formate_articles = formatted_articles(three_articles)
        for articles in formate_articles:
            message = client.messages.create(
            from_='+15074195966',
            body=f"{COMPANY_NAME}:{up_down}{abs(percentage_change)}%\n{articles}",
            to='+919316551262')
