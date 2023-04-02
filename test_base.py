import pytest

from Pages.checkbox_page import CheckboxPageObject
from Pages.textbox_page import TextBoxPageObject
from Pages.main_page import MainPageObject
from util.constants import Constants


class TestBase:
    @pytest.fixture(scope='class', autouse=True)
    def before_all(self, get_browser):
        global main_page
        global textbox_page
        global checkbox_page
        global browser
        browser = get_browser
        main_page = MainPageObject(browser, Constants.link_site)
        textbox_page = TextBoxPageObject(browser, Constants.link_site)
        checkbox_page = CheckboxPageObject(browser, Constants.link_site)
        main_page.open()

    @staticmethod
    def get_main_page():
        return main_page

    @staticmethod
    def get_textbox_page():
        return textbox_page

    @staticmethod
    def choose_elements():
        main_page.click_elements_button()

    @staticmethod
    def get_checkbox_page():
        return checkbox_page
