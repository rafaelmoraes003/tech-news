from tech_news.database import find_news
from tech_news.analyzer.search_engine import get_news_tuples
from collections import Counter


# Requisito 10
def top_5_news():
    news_list = find_news()
    sorted_list = sorted(
        news_list,
        key=lambda x: (x["comments_count"], x["title"]),
        reverse=True,
    )

    if len(sorted_list) <= 5:
        return get_news_tuples(sorted_list)

    top_five_news_list = []

    for i in range(5):
        top_five_news_list.append(sorted_list[i])

    return get_news_tuples(top_five_news_list)


# Requisito 11
def top_5_categories():
    news_list = find_news()

    categories = [news["category"] for news in news_list]

    most_common_categories = Counter(categories).most_common(5)

    sorted_categories = sorted(
        most_common_categories, key=lambda x: (-x[1], x[0])
    )

    return [category[0] for category in sorted_categories]
