import pytest
from test_base import TestBase
from util.constants import Constants


class TestEndToEnd(TestBase):
    @pytest.fixture(scope='class', autouse=True)
    def env_preparation(self):
        global main_page
        global checkbox_page
        main_page = super().get_main_page()
        checkbox_page = super().get_checkbox_page()

    def test_successful_choose_checkbox(self):
        super().choose_elements()
        checkbox_page.click_checkbox_button()

