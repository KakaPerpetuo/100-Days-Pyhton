import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

account_sid = '[ACCOUNT_SID]'
auth_token = '[TWILIO_AUTH_TOKEN]'

alpha_vantage_api_key = "[ENCRYPTION_KEY]"
alpha_vantage_url = "https://www.alphavantage.co/query"

newsapi_api_key = "[ENCRYPTION_KEY]"
newsapi_url = "https://newsapi.org/v2/everything"

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

alpha_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_vantage_api_key,
}

response_alpha = requests.get(alpha_vantage_url, params=alpha_parameters)
response_alpha.raise_for_status()
data_alpha = response_alpha.json()["Time Series (Daily)"]
data_alpha_list =[value for (key, value) in data_alpha.items()]
yesterday = data_alpha_list[0]
day_before_yesterday = data_alpha_list[1]

yesterday_close = float(yesterday["4. close"])    
day_before_yesterday_close = float(day_before_yesterday["4. close"])

if (yesterday_close - day_before_yesterday_close) / day_before_yesterday_close > 0.05 or (yesterday_close - day_before_yesterday_close) / day_before_yesterday_close < -0.05:
    ## STEP 2: Use https://newsapi.org
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
    newsapi_parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": newsapi_api_key,
    }
    
    response_news = requests.get(newsapi_url, params=newsapi_parameters)
    response_news.raise_for_status() 
    data_articles = response_news.json()["articles"]

    percentage_change = ((yesterday_close - day_before_yesterday_close) / day_before_yesterday_close) 
    
    three_news = data_articles[:3]

    message_body = [f"Headline: {article['title']}\nBrief: {article['description']}" for article in three_news]
    
    if percentage_change > 0:
        percentage_change = "🔺 " + str(percentage_change)
    else:
        percentage_change = "🔻 " + str(percentage_change)

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        from_="[PHONE_NUMBER]",
        body=f"{STOCK}: {percentage_change*100}%\n{message_body[0]}\n\n{message_body[1]}\n\n{message_body[2]}",
        to="[PHONE_NUMBER]",
    )
    print(message.status)
 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""


