from selenium.webdriver.common.by import By


class MainPage:
    BUTTON_ELEMENTS = (By.CSS_SELECTOR, 'div.card.mt-4.top-card')


class TextBox:
    BUTTON_TEXT_BOX = (By.ID, 'item-0')
    FULL_NAME_TEXT_BOX = (By.ID, 'userName')
    EMAIL_TEXT_BOX = (By.ID, 'userEmail')
    CURRENT_ADDRESS_TEXT_BOX = (By.ID, 'currentAddress')
    PERMANENT_ADDRESS_TEXT_BOX = (By.ID, 'permanentAddress')
    BUTTON_SUBMIT = (By.ID, 'submit')
    FIELD_WITH_RESULTS = (By.ID, 'output')
    RESULT_FIELD_WITH_INFO = (By.CLASS_NAME, 'border')

class Checkbox:
    BUTTON_CHECKBOX = (By.ID, 'item-1')
