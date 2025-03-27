from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class BrandsPage(BasePage):
    BRAND_TEXT = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')
    BRAND_PRODUCTS = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div')
    BRANDS_SECTION = (By.XPATH, '/html/body/section/div/div[2]/div[1]/div/div[2]/div')

    TIMEOUT = ReadConfig.get_timeout_value()


    def brand_page_is_visible(self):
        brand_text = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BRAND_TEXT))

        return brand_text.is_displayed()

    def brand_products_are_visible(self):
        products = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BRAND_PRODUCTS))

        return products.is_displayed()


    def verify_brands_are_visible(self):
        brands = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BRANDS_SECTION))

        return brands.is_displayed()


    def click_brand(self, brand_number):
        brands = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BRANDS_SECTION)).find_elements(By.TAG_NAME, 'a')

        brands[brand_number - 1].click()
        time.sleep(3)
        return self

