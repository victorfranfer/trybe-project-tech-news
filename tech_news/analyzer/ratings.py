from tech_news.database import find_news
from collections import Counter


# Requisito 10
def top_5_categories():
    news = []
    for article in find_news():
        news.append(article["category"])

    categories_counter = Counter(news).most_common(5)
    sorted_categories_list = sorted(categories_counter,
                                    key=lambda x: (-x[1], x[0]))
    slice_categories = [tuple[0] for tuple in sorted_categories_list]

    return slice_categories
