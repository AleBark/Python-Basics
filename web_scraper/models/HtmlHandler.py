# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

"""
Ale Bark Bruneri
"""


class HtmlHandler(object):

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Firefox()
        self.driver.get(url)
        self.html = self.driver.page_source

    def get_html(self):
        return self.html

    def maximize_window(self):
        self.driver.maximize_window()

    def dismiss_popup(self, id):
        self.driver.find_element_by_id(id).click()

    def scroll_page_down(self, path, scroll_quantity):
        component = self.driver.find_element_by_xpath(path)
        for x in range(scroll_quantity):
            component.send_keys(Keys.PAGE_DOWN)

    def is_visible_in_viewport_by_class_name(self, classname):
        element = self.driver.find_element_by_class_name(classname)
        return self.driver.execute_script(
            "var elem = arguments[0],                 " +
            "  box = elem.getBoundingClientRect(),    " +
            "  cx = box.left + box.width / 2,         " +
            "  cy = box.top + box.height / 2,         " +
            "  e = document.elementFromPoint(cx, cy); " +
            "for (; e; e = e.parentElement) {         " +
            "  if (e === elem)                        " +
            "    return true;                         " +
            "}                                        " +
            "return false;                            ", element)
