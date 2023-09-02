import requests
from bs4 import BeautifulSoup

from utils.config import MAIN_URL


def get_scrape():
    r = requests.get(
        MAIN_URL,
        verify=False,
        headers={
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "Referer": "https://www.google.com/",
        },
    )

    return BeautifulSoup(r.text, "lxml")
