import requests
from parsel import Selector
from time import sleep
from tech_news.database import create_news


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, headers={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.Timeout):
        return None
    else:
        return response.text


# Requisito 2
def scrape_updates(html_content):
    selector = Selector(text=html_content)

    news_urls = [
        news.css("a::attr(href)").get()
        for news in selector.css("#content article")
    ]

    return news_urls


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)

    next_page_url = selector.css(".next::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_news(html_content):
    selector = Selector(text=html_content)

    news = {}

    news["url"] = selector.css("link[rel=canonical]::attr(href)").get()
    news["title"] = selector.css(".entry-title::text").get().strip()
    news["timestamp"] = selector.css(".meta-date::text").get()
    news["writer"] = selector.css(".author a::text").get()

    comments_count = selector.css(".post-comments .title-block::text").get()
    news["comments_count"] = (
        int(comments_count.strip().split(" ")[0]) if comments_count else 0
    )

    news["summary"] = "".join(
        selector.css(".entry-content > p:first-of-type *::text").getall()
    ).strip()

    tags = selector.css(".post-tags ul li a::text").getall()
    news["tags"] = tags if tags else []

    news["category"] = selector.css(".entry-details span.label::text").get()

    return news


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news = []

    i = 0

    while len(news) < amount:
        html_content = fetch(url)
        news_urls = scrape_updates(html_content)

        try:
            news.append(scrape_news(fetch(news_urls[i])))
            i += 1
        except IndexError:
            url = scrape_next_page_link(html_content)
            i = 0

    create_news(news)
    return news
