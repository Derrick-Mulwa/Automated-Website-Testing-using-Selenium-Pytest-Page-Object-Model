from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class CategoryProductsPage(BasePage):
    CATEGORY_PRODUCTS_PAGE = (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/h2')
    MEN_ITEMS = (By.XPATH, '//*[@id="accordian"]/div[2]/div[1]/h4/a/span')
    MEN_ITEMS_SUBCAT = (By.XPATH, '//*[@id="Men"]/div/ul')
    SOMETHING = (By.XPATH, 'Women')
    SOMETHING = (By.XPATH, 'Women')

    TIMEOUT = ReadConfig.get_timeout_value()

    def category_text_is_visible(self):
        category_text = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CATEGORY_PRODUCTS_PAGE))

        return category_text.is_displayed()

    def click_men_items(self):
        men_items = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.MEN_ITEMS))

        time.sleep(3)

        men_items.click()

    def click_men_subcategory(self, number):
        items = self.driver.find_element(*self.MEN_ITEMS_SUBCAT).find_elements(By.TAG_NAME, 'a')
        item_to_click = items[number - 1]
        if item_to_click.is_displayed():
            item_to_click.click()
        else:
            self.click_men_items()
            time.sleep(2)
            item_to_click.click()