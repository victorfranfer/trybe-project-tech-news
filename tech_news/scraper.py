import requests
from parsel import Selector
from time import sleep
import re
from .database import create_news


# Requisito 1
def fetch(url):
    user_agent = {"user-agent": "Fake user-agent"}
    kwargs = {"url": url, "timeout": 3, "headers": user_agent}
    try:
        page = requests.get(**kwargs)
        sleep(1)
        if page.status_code != 200:
            return None
        return page.text
    except requests.exceptions.RequestException:
        return None


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(html_content)
    updates = selector.css(".entry-title > a::attr(href)").getall()
    return updates


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(html_content)
    response = selector.css(".next::attr(href)").get()

    if not response:
        return None
    return response


# Requisito 4
def scrape_news(html_content):
    url = Selector(html_content).css("link[rel='canonical']::attr(href)").get()
    title = Selector(html_content).css(".entry-title::text").get().strip()
    timestamp = Selector(html_content).css(".meta-date::text").get()
    writer = Selector(html_content).css(".url.fn.n::text").get()
    reading_time_string = (
        Selector(html_content).css(".meta-reading-time::text").get()
    )
    reading_time = int(re.sub("[^0-9]", "", reading_time_string))
    summary = (
        Selector(html_content).xpath("//p").xpath("string()").get().strip()
    )
    category = Selector(html_content).css(".meta-category .label::text").get()
    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": reading_time,
        "summary": summary,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://blog.betrybe.com/"
    news = []
    counter = 0

    while counter < amount:
        response = fetch(URL_BASE)
        updates = scrape_updates(response)

        for article in updates:
            response_fetch = fetch(article)
            data = scrape_news(response_fetch)
            news.append(data)
            counter += 1
            if counter == amount:
                break
        URL_BASE = scrape_next_page_link(response)
    create_news(news)
    return news
