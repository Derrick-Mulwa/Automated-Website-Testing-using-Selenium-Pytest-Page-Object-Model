from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.base_page import BasePage
import time


class AccountCreatedPage(BasePage):
    ACCOUNT_CREATED = (By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    CONTINUE = (By.XPATH, '//*[@id="form"]/div/div/div/div/a')

    def account_created_is_visible(self):
        account_created = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(self.ACCOUNT_CREATED))

        return account_created.is_displayed()

    def click_continue_button(self):
        self.driver.find_element(*self.CONTINUE).click()
        time.sleep(3)
        return self

