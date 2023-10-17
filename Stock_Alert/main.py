import requests
import os

STOCK_SYMBOL = "OTLY"
COMPANY_NAME = "Oatly"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_api_key = os.environ.get("STOCK_API_KEY")
news_api_key = os.environ.get("NEWS_API_KEY")

# Get hold of the API endpoint of Alphavantage.
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_SYMBOL,
    "outputsize": "compact",
    "apikey": stock_api_key
}

stock_response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data = stock_response.json()["Time Series (Daily)"]

# Get hold of the actual yesterday's stock_data (independent of the actual date).
data_list = [value for (key, value) in stock_data.items()]
yesterday_data = data_list[0]
day_before_yesterday_data = data_list[1]

# Get hold of the closing price of yesterday and the day before yesterday.
price_yesterday = yesterday_data["4. close"]
price_day_before_yesterday = day_before_yesterday_data["4. close"]
recent_closing_price = float(price_yesterday)
previous_closing_price = float(price_day_before_yesterday)

# Get the current difference between the recent closing price and the previous closing price in percentage.
percentage_change = ((recent_closing_price - previous_closing_price) / previous_closing_price) * 100
percentage = f"{round(percentage_change, 2)} %"
print(f"My Stock Alert\n\n{COMPANY_NAME}: {percentage}\n\n")

# If the stock price increases/decreases by 5% between yesterday and the day before yesterday,
# then get the latest three news articles.
if recent_closing_price <= previous_closing_price * 0.95 or recent_closing_price >= previous_closing_price * 1.05:

    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    three_articles = news_response.json()["articles"][:3]

    list_articles = [f"Headline: {article['title']}\nBrief: {article['description']}\n"
                     f"Read the full article here: {article['url']}" for article in three_articles]
    print(f"{list_articles[0]}\n\n{list_articles[1]}\n\n{list_articles[2]}")


# You can modify this code using the 'smtplib' module and store the code in a cloud (e.g. pythonanywhere)
# so that you can send yourself daily E-Mail Alerts.
# Here the additional code for sending an E-Mail:

# import smtplib

#     my_email = "testmail@mailprovider.com"
#     password = "mypassword"

## Get hold of the smtp address for your email provider:
#     with smtplib.SMTP("smtp.mailprovider.com", port="myportnumber") as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(
#             from_addr=my_email, to_addrs="recipient@mailprovider.com",
#             msg=f"Subject: My Stock Alert\n\n{COMPANY_NAME}: {percentage}"
#                 f"\n\n{list_articles[0]}\n\n{list_articles[1]}\n\n{list_articles[2]}"
#         )
