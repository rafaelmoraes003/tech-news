import requests
from time import sleep


# Requisito 1
def fetch(url):
    sleep(1)
    try:
        response = requests.get(
            url, header={"user-agent": "Fake user-agent"}, timeout=3
        )
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.Timeout):
        return None
    else:
        return response.text
    #


# Requisito 2
def scrape_updates(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
