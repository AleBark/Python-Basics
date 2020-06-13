# -*- coding: utf-8 -*-
import time

from models.HtmlHandler import HtmlHandler
from bs4 import BeautifulSoup

"""
Ale Bark Bruneri
"""


def main():
    html_handler = HtmlHandler(
        "https://startupbase.com.br/home/startups?q=&states=all&cities=all&segments=all&targets=all&phases=all&models=all&badges=all")
    #html = html_handler.get_html()

    html_handler.maximize_window()
    html_handler.dismiss_popup('onesignal-popover-cancel-button')
    time.sleep(5)

    while not html_handler.is_visible_in_viewport_by_class_name('sbfooter'):
        html_handler.scroll_page_down('/html/body', 5)

        # This will prevent fast scrolling which will cause the footer to visible
        # for a very short period (causing the while loop to break) before the script load more items
        time.sleep(2)


if __name__ == '__main__':
    main()
