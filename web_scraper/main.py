# -*- coding: utf-8 -*-
from web_scraper.models.HtmlHandler import HtmlHandler
from bs4 import BeautifulSoup

"""
Ale Bark Bruneri
"""


def main():
    html_handler = HtmlHandler("https://pixabay.com/pt/images/search/")
    html = html_handler.get_html()

    soup = BeautifulSoup(html, 'html.parser')
    div_items = soup.find('div', attrs={'class': 'search_results'})
    images = len(list(div_items.children))

    print("Total images:" + str(images))
    print("")
    print("Top 5 downloads:")

    # I know, terrible
    cont = 0

    if images > 0:
        for item in div_items.find_all('img'):
            if cont >= 5:
                return
            print("Description: " + item.attrs['alt'])
            print("Links: " + item.attrs['srcset'])
            print("")
            cont = cont + 1


if __name__ == '__main__':
    main()