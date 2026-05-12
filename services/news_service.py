import os
import requests

from dotenv import load_dotenv

load_dotenv()

NEWS_API_KEY = os.getenv("NEWS_API_KEY")


def get_stock_news(ticker: str):

    url = (
        f"https://newsapi.org/v2/everything?"
        f"q={ticker}&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    )

    response = requests.get(url)

    data = response.json()

    articles = data.get("articles", [])

    news = []

    for article in articles[:5]:

        news.append({
            "title": article.get("title"),
            "source": article.get("source", {}).get("name"),
            "url": article.get("url")
        })

    return news