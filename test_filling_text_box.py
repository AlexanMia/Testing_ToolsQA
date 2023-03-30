import pytest
from test_base import TestBase
from util.constants import Constants


class TestEndToEnd(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global main_page
        global textbox_page
        main_page = super().get_main_page()
        textbox_page = super().get_elements_page()

    def test_successful_filling_text_box(self):
        super().choose_elements()
        textbox_page.click_text_box_button()
        textbox_page.entering_text_into_boxes()
        assert textbox_page.find_field_with_entering_values(), 'THERE WASN\'T FIELD WITH THE RESULTS'

    @pytest.mark.parametrize('constant',
                             [('Name:' + Constants.Full_Name),
                              ('Email:' + Constants.Email),
                              ('Current Address :' + Constants.Current_address),
                              ('Permananet Address :' + Constants.Permananet_address)])
    def test_right_text_in_result_field(self, constant):
        assert constant in textbox_page.get_text(), f'Entering name {constant} ' \
                                                    f'does not match in the field {textbox_page.get_text()}'
