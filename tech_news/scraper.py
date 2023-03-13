import requests
from parsel import Selector
from time import sleep


URL_BASE = "https://blog.betrybe.com/"


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
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
