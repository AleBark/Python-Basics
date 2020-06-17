# -*- coding: utf-8 -*-
from seleniumwire import webdriver


"""
Ale Bark Bruneri
"""


class RequestHandler(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)

    def intercept(self):
        if len(self.driver.requests) > 0:
            for request in self.driver.requests:
                if request.method == 'POST':
                    a = request
                    print(
                        request.response.status_code,
                        request.response.body, "\n"
                    )
