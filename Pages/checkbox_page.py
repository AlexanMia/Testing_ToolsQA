from Pages.base_page import BasePage
from util.constants import Constants
from util.locators import Checkbox


class CheckboxPageObject(BasePage):
    def click_checkbox_button(self):
        super().element_click(Checkbox.BUTTON_CHECKBOX)
