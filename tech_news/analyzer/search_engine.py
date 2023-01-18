from tech_news.database import search_news
from datetime import datetime


def get_news_tuples(news_list):
    news_tuples = [tuple((news["title"], news["url"])) for news in news_list]
    return news_tuples


# Requisito 6
def search_by_title(title):
    news_list = search_news({"title": {"$regex": title, "$options": "i"}})
    news = get_news_tuples(news_list)
    return news


# Requisito 7
def search_by_date(date):
    try:
        query_date = datetime.strptime(date, "%Y-%m-%d").strftime("%d/%m/%Y")
    except ValueError:
        raise ValueError("Data inválida")
    else:
        news_list = search_news(
            {"timestamp": {"$regex": query_date, "$options": "i"}}
        )
        news = get_news_tuples(news_list)
        return news


# Requisito 8
def search_by_tag(tag):
    news_list = search_news({"tags": {"$regex": tag, "$options": "i"}})
    news = get_news_tuples(news_list)
    return news


# Requisito 9
def search_by_category(category):
    news_list = search_news(
        {"category": {"$regex": category, "$options": "i"}}
    )
    news = get_news_tuples(news_list)
    return news
