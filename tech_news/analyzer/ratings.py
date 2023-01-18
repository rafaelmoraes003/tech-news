from tech_news.database import find_news
from tech_news.analyzer.search_engine import get_news_tuples


# Requisito 10
def top_5_news():
    news = find_news()
    sorted_list = sorted(
        news, key=lambda x: (x["comments_count"], x["title"]), reverse=True
    )

    if len(sorted_list) <= 5:
        return get_news_tuples(sorted_list)

    top_five_news_list = []

    for i in range(5):
        top_five_news_list.append(sorted_list[i])

    return get_news_tuples(top_five_news_list)


print(top_5_news())


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
