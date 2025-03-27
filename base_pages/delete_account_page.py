from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_pages.base_page import BasePage
import time


class DeleteAccountPage(BasePage):
    ACCOUNT_DELETED = (By.XPATH, '//*[@id="form"]/div/div/div/h2/b')
    CONTINUE = (By.XPATH, '//*[@id="form"]/div/div/div/div/a')

    def account_deleted_is_visible(self):
        account_deleted = WebDriverWait(self.driver, 30).until(
            EC.visibility_of_element_located(self.ACCOUNT_DELETED))

        return account_deleted.is_displayed()


    def click_continue(self):
        self.driver.find_element(*self.CONTINUE).click()
        time.sleep(3)
        return self
