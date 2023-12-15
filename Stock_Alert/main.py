import requests
from news_request import get_news_data, show_latest_articles, COMPANY_NAME
from decimal import Decimal
import os

STOCK_SYMBOL = "OTLY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"


# Get hold of the API endpoint of Alphavantage.
def get_stock_data():
    stock_api_key = os.environ.get("STOCK_API_KEY")

    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK_SYMBOL,
        "outputsize": "compact",
        "apikey": stock_api_key
    }

    stock_response = requests.get(STOCK_ENDPOINT, params=stock_params).json()

# When using a wrong API key for the API endpoint of Alpha Vantage,
# it currently returns still the status code 200.
# The following workaround catches the wrong input as long as the stock_response contains the key 'Error Message'.
    if 'Error Message' in stock_response:
        raise KeyError(f"{stock_response['Error Message']}")
    else:
        return stock_response["Time Series (Daily)"]


stock_data = get_stock_data()


# Get hold of the closing price of yesterday and the day before yesterday.
def get_closing_price_for_yesterday_and_day_before_yesterday():
    data_list = list(stock_data.values())
    price_yesterday = data_list[0]["4. close"]
    price_day_before_yesterday = data_list[1]["4. close"]
    closing_price_yesterday = Decimal(price_yesterday)
    previous_closing_price = Decimal(price_day_before_yesterday)
    return closing_price_yesterday, previous_closing_price


closingPriceYesterday, previousClosingPrice = get_closing_price_for_yesterday_and_day_before_yesterday()


# Get the current difference between the recent closing price and the previous closing price in percentage.
def calculate_percentage():
    percentage_change = ((closingPriceYesterday - previousClosingPrice) / previousClosingPrice) * 100
    percentage = round(percentage_change, 2)
    return percentage


percentage_stock = calculate_percentage()

print(f"My Stock Alert\n\n{COMPANY_NAME}: {percentage_stock} %\n\n")


# If the stock price increases/decreases by 5% between yesterday and the day before yesterday,
# then get the latest three news articles.
def add_latest_news():
    if percentage_stock >= 5 or percentage_stock <= -5:
        get_news_data()
        return show_latest_articles()


print(add_latest_news())

# You can modify this code using the 'smtplib' module and store the code in a cloud (e.g. pythonanywhere)
# so that you can send yourself daily E-Mail Alerts.
# Here the additional code for sending an E-Mail:

# import smtplib

# my_email = "testmail@mailprovider.com"
# password = "mypassword"

# Get hold of the smtp address for your email provider:
#   with smtplib.SMTP("smtp.mailprovider.com", port="myportnumber") as connection:
#       connection.starttls()
#       connection.login(user=my_email, password=password)
#       connection.sendmail(
#       from_addr=my_email, to_addrs="recipient@mailprovider.com", \
#           msg=f"Subject: My Stock Alert\n\n{COMPANY_NAME}: {percentage}"
#       f"\n\n{list_articles[0]}\n\n{list_articles[1]}\n\n{list_articles[2]}")
