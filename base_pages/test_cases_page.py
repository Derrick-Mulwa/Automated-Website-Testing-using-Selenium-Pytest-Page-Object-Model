from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class PageTestCases(BasePage):
    TEST_CASES = (By.XPATH, '//*[@id="form"]/div/div[1]/div/h2/b')

    TIMEOUT = ReadConfig.get_timeout_value()

    def test_cases_page_is_visible(self):
        test_cases_page = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.TEST_CASES))

        return test_cases_page.is_displayed()
