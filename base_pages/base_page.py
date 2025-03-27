import time
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def navigate_to(self, url):
        self.driver.get(url)
        time.sleep(6)
        return self

    def verify_page_title(self, expected_title):
        return expected_title in self.driver.title
