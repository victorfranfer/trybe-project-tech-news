from tech_news.database import get_collection
from collections import Counter


# Requisito 10
def top_5_categories():
    news = []
    for article in get_collection():
        news.append(article["category"])

    categories_counter = Counter(news)
    sorted_categories_list = sorted(categories_counter.items(),
                                    key=lambda x: x[1], reverse=True)
    return sorted_categories_list
