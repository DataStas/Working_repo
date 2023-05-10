import requests
from datetime import datetime as dt

STOCK = "TSLA"
COMPANY_NAME = "Tesla"

alpha_API = 'QXK62BKH47SWE22P'
alpha_End_point = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY'
news_API = '46548c537aa24743b510b83587f02d9c'
news_end_point = 'https://newsapi.org/v2/everything'

## STEP 1: Use https://newsapi.org
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
def check_stock():
    alpha_parameters = {
    "function": "TIME_SERIES_INTRADAY",
    'symbol': STOCK,
    'interval': "60min",
    'apikey': alpha_API
    }
    response = requests.get(url=alpha_End_point,
                            params=alpha_parameters)
    print(response.status_code)
    data_stocks = response.json()

    yesterday = dt(year=dt.now().year,
            month=dt.now().month,
            day=dt.now().day-1,
            hour=5,
            minute=0,
            second=0)
    day_before = dt(year=dt.now().year,
            month=dt.now().month,
            day=dt.now().day-2,
            hour=5,
            minute=0,
            second=0)


    yesterday_price = float(data_stocks['Time Series (60min)'][str(yesterday)]['1. open'])
    day_before_price = float(data_stocks['Time Series (60min)'][str(day_before)]['1. open'])

    if abs(yesterday_price-day_before_price)/yesterday_price*100 >= 1:
        return True


## STEP 2: Use https://www.alphavantage.co
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
def get_news():
    day = dt(year=dt.now().year,
            month=dt.now().month,
            day=dt.now().day-1)
    
    news_parameters = {
        'q': COMPANY_NAME,
        'from': day,
        'sortBy': 'popularity',
        'apiKey': news_API
    }
    
    news_response = requests.get(url=news_end_point,
                                 params=news_parameters)
    news_response.raise_for_status()
    # print(news_response.url)
    print(news_response.status_code)
    news_data = news_response.json()
    print(news_data['articles'][0]['source']['name'], news_data['articles'][0]['author'])
    print(news_data['articles'][0]['title'])
    print(news_data['articles'][0]['description'])

if check_stock():
    get_news()