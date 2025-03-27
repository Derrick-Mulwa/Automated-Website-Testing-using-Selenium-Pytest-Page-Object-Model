from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class PaymentsDonePage(BasePage):
    ORDER_PLACED_TEXT = (By.XPATH, '//*[@id="form"]/div/div/div/h2')
    CONGRATULATIONS_YOUR_ORDER_TEXT = (By.XPATH,'//*[@id="form"]/div/div/div/p')
    DELETE_ACCOUNT_BUTTON = (By.XPATH,'//*[@id="header"]/div/div/div/div[2]/div/ul/li[5]/a')
    DOWNLOAD_INVOICE_BUTTON = (By.XPATH, '//*[@id="form"]/div/div/div/a')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="form"]/div/div/div/div/a')

    TIMEOUT = ReadConfig.get_timeout_value()

    def order_placed_text_is_visible(self):
        order_placed_text = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.ORDER_PLACED_TEXT))

        return order_placed_text.is_displayed()

    def congratulations_your_order_is_visible(self):
        congratulations = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CONGRATULATIONS_YOUR_ORDER_TEXT))

        return congratulations.is_displayed()

    def click_delete_account_button(self):
        delete_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.DELETE_ACCOUNT_BUTTON))

        delete_btn.click()
        return self

    def click_download_invoice_button(self):
        btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.DOWNLOAD_INVOICE_BUTTON))

        btn.click()
        time.sleep(4)
        return self

    def click_continue_button(self):
        btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CONTINUE_BUTTON))

        btn.click()
        return self

