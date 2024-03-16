import requests
from bs4 import BeautifulSoup
from time import sleep

data = {
        'device': 'OS X Chrome v.88.0.4389.90 3a7a0',
        'app_version': '870'
    }

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'
    }


def get_offers(max_page):
    offers = []
    for page_number in range(1, max_page+1):
        try:
            sleep(0.5)
            url = f'https://www.pepper.ru/?page={page_number}&ajax=true&layout=horizontal'
            response = requests.get(url, headers=headers, data=data).json()
        except Exception:
            return False

        soup = BeautifulSoup(response["data"]["content"], "html.parser")

        try:
            sales = soup.select("article.thread.cept-thread-item.thread--type-list.imgFrame-container--scale")

            for item in sales:
                if "thread--expired" in item.get("class") or "js-telegram-widget" in item.get("class") or "thread--discussion" in item.get("class"):
                    continue

                link_and_name = item.find("a", class_="cept-tt")

                link = link_and_name.get("href")
                name = link_and_name.get("title")
                temperature = item.find("span", class_="cept-vote-temp").text.replace("\n", "").replace("\t", "")

                offers.append([name, link, temperature])
        except Exception:
            return False

    return offers
