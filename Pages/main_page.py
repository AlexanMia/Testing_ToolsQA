from Pages.base_page import BasePage
from util.locators import MainPage


class MainPageObject(BasePage):
    def click_elements_button(self):
        super().element_click(MainPage.BUTTON_ELEMENTS)
