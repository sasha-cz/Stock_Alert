# Get the latest three news articles from a NEWS_ENDPOINT.
import requests
import os

COMPANY_NAME = "Oatly"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


def get_news_data():
    news_api_key = os.environ.get("NEWS_API_KEY")
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
        "language": "en",
        "sortBy": "publishedAt",
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params).json()
    return news_response


def show_latest_articles():
    articles = get_news_data()["articles"][:3]
    list_articles = [f"Headline: {article['title']}\nBrief: {article['description']}\n"
                     f"Read the full article here: {article['url']}" for article in articles]

    return f"{list_articles[0]}\n\n{list_articles[1]}\n\n{list_articles[2]}"
