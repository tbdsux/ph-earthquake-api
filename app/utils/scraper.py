import requests
from bs4 import BeautifulSoup


def get_scrape(url: str):
    try:
        r = requests.get(
            url,
            verify=False,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
                "Referer": "https://www.google.com/",
            },
        )

        if not r.ok:
            raise Exception("Failed to fetch page, does the page exists?")

        r.encoding = "utf-8"  # force utf-8 encoding

        return [True, BeautifulSoup(r.text, "lxml")]
    except Exception as e:
        return [False, str(e)]
