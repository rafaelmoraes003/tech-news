from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_category,
    search_by_tag,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories
import sys

options = [
    "Popular o banco com notícias;",
    "Buscar notícias por título;",
    "Buscar notícias por data;",
    "Buscar notícias por tag;",
    "Buscar notícias por categoria;",
    "Listar top 5 notícias;",
    "Listar top 5 categorias;",
    "Sair.",
]

responses = {
    "0": {
        "message": "Digite quantas notícias serão buscadas:",
        "action": lambda amount: get_tech_news(int(amount)),
    },
    "1": {
        "message": "Digite o título:",
        "action": lambda title: search_by_title(title),
    },
    "2": {
        "message": "Digite a data no formato aaaa-mm-dd:",
        "action": lambda date: search_by_date(date),
    },
    "3": {
        "message": "Digite a tag:",
        "action": lambda tag: search_by_tag(tag),
    },
    "4": {
        "message": "Digite a categoria:",
        "action": lambda category: search_by_category(category),
    },
    "5": {"message": None, "action": lambda: top_5_news()},
    "6": {"message": None, "action": lambda: top_5_categories()},
}


def create_menu():
    init_options_str = "Selecione uma das opções a seguir:\n"
    for i in range(len(options)):
        init_options_str += f" {i} - {options[i]}\n"
    print(init_options_str)


# Requisito 12
def analyzer_menu():
    create_menu()

    option = input()

    if option == "7":
        print("Encerrando script")
        return

    if option in ["5", "6"]:
        print(responses[option]["action"]())
        return

    try:
        print(responses[option]["message"])
    except KeyError:
        print("Opção inválida", file=sys.stderr)
        return

    action = input()
    print(responses[option]["action"](action))


if __name__ == "__main__":
    analyzer_menu()
