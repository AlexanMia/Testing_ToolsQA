import pytest

from Pages.textbox_page import TextBoxPageObject
from Pages.main_page import MainPageObject
from util.constants import Constants


class TestBase:
    @pytest.fixture(scope='class', autouse=True)
    def before_all(self, get_browser):
        global main_page
        global elements_page
        global browser
        browser = get_browser
        main_page = MainPageObject(browser, Constants.link_site)
        elements_page = TextBoxPageObject(browser, Constants.link_site)
        main_page.open()

    @staticmethod
    def get_main_page():
        return main_page

    @staticmethod
    def get_elements_page():
        return elements_page

    @staticmethod
    def choose_elements(self):
        main_page.click_elements_button()
