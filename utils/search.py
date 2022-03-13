import time
from selenium.webdriver.common.by import By

class SearchTests:
    # URL
    URL = "https://www.reserved.com/ro/ro/"

    SEARCH_CLICK = (By.CSS_SELECTOR, '.action-btn__SearchWrapper-zbpc1m-4.eNpASB.verB')
    SEARCH_FIELD = (By.CSS_SELECTOR, '.input__InputText-sc-1mxde2b-0.ipFxa.search-box__StyledTextField-sc-19imnj1-0.hzAHJR')
    ACCEPT_COOKIES_BUTTON = (By.ID, 'cookiebotDialogOkButton')

    def __init__(self, browser):
        self.browser = browser

    def load_page(self):
        self.browser.get(self.URL)
        self.browser.find_element(*self.ACCEPT_COOKIES_BUTTON).click()

    def search_click(self, pijama):
        self.browser.find_element(*self.SEARCH_CLICK).click()
        self.browser.find_element(*self.SEARCH_FIELD).send_keys(pijama)
        time.sleep(3)


