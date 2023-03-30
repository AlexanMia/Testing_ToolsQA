from Pages.base_page import BasePage
from util.constants import Constants
from util.locators import TextBox


class TextBoxPageObject(BasePage):
    def click_text_box_button(self):
        super().element_click(TextBox.BUTTON_TEXT_BOX)

    def entering_text_into_boxes(self):
        super().enter_value_into_box(TextBox.FULL_NAME_TEXT_BOX, Constants.Full_Name)
        super().enter_value_into_box(TextBox.EMAIL_TEXT_BOX, Constants.Email)
        super().enter_value_into_box(TextBox.CURRENT_ADDRESS_TEXT_BOX, Constants.Current_address)
        super().enter_value_into_box(TextBox.PERMANENT_ADDRESS_TEXT_BOX, Constants.Permananet_address)
        super().element_click(TextBox.BUTTON_SUBMIT)

    def find_field_with_entering_values(self):
        return super().find_need_element(TextBox.FIELD_WITH_RESULTS)

    def get_text(self):
        return super().get_elements_text(TextBox.RESULT_FIELD_WITH_INFO)
