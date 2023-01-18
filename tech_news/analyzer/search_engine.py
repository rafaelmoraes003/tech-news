from tech_news.database import search_news


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
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
