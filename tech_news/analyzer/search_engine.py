from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    news = []
    for article in search_news(query):
        news.append((article["title"], article["url"]))
    return news


# Requisito 8
def search_by_date(date):
    try:
        date_object = datetime.strptime(date, "%Y-%m-%d")
        new_format_date = date_object.strftime("%d/%m/%Y")
        query = {"timestamp": {"$regex": new_format_date, "$options": "i"}}
        news = []
        for article in search_news(query):
            news.append((article["title"], article["url"]))
        return news
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 9
def search_by_category(category):
    query = {"category": {"$regex": category, "$options": "i"}}
    news = []
    for article in search_news(query):
        news.append((article["title"], article["url"]))
    return news
