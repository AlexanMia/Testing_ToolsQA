class BasePage:
    def __init__(self, browser, url, timeout=30):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def find_need_element(self, locator):
        return self.browser.find_element(*locator)

    def element_click(self, locator):
        return self.find_need_element(locator).click()

    def enter_value_into_box(self, locator, meaning):
        return self.find_need_element(locator).send_keys(meaning)

    def get_elements_text(self, locator):
        return self.find_need_element(locator).text
