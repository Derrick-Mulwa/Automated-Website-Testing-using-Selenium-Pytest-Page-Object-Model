from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
from base_pages.base_page import BasePage
from utilities.read_properties import ReadConfig


class AllProductsPage(BasePage):
    SALE_IMAGE = (By.ID, 'sale_image')
    PRODUCT_LIST = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div')
    VIEW_PRODUCT_BUTTON = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/div[2]/div/div[2]/ul/li/a')
    SEARCH_TEXT_INPUT = (By.ID, 'search_product')
    SEARCH_BUTTON = (By.ID, 'submit_search')
    SEARCHED_PRODUCTS_TEXT = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div/h2')
    SEARCHED_PRODUCTS_LIST = (By.XPATH, '/html/body/section[2]/div/div/div[2]/div')

    PRODUCT_XPATH_PRE = '/html/body/section[2]/div[1]/div/div[2]/div/div'
    PRODUCT_XPATH_POST = '/div/div[1]/div[1]'
    ADD_TO_CART_XPATH_POST = '/div/div[1]/div[2]/div/a'
    CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button')
    VIEW_CART_BUTTON = (By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[2]/a')
    BRANDS_SECTION = (By.XPATH, '/html/body/section[2]/div[1]/div/div[1]/div/div[3]')

    ALL_PRODUCTS_TEXT = (By.XPATH, '/html/body/section[2]/div[1]/div/div[2]/div/h2')
    CART_BUTTON = (By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a')
    SOMETHING = (By.XPATH,)
    SOMETHING = (By.XPATH,)

    TIMEOUT = ReadConfig.get_timeout_value()

    def navigated_to_all_products_page_successfully(self):
        return 'All Products' in self.driver.title

    def product_list_is_visible(self):
        product_list = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PRODUCT_LIST))

        return product_list.is_displayed()

    def click_view_product_button(self):
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.VIEW_PRODUCT_BUTTON))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", button)

        button.click()

        return self

    def enter_search_text(self, search_text):
        search_input_field = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCH_TEXT_INPUT))

        search_input_field.clear()
        search_input_field.send_keys(search_text)

        return self

    def click_search_button(self):
        search_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCH_BUTTON))

        search_btn.click()

        return self

    def searched_products_text_is_visible(self):
        searched_products = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCHED_PRODUCTS_TEXT))

        return searched_products.is_displayed()

    def searched_products_list_is_visible(self):
        searched_products_list = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.SEARCHED_PRODUCTS_LIST))
        num_children = searched_products_list.find_elements("xpath", "./*")
        if len(num_children)>2:
            return True
        else:
            return False

    def hover_and_add_to_cart(self, product_number):
        # product_number is 1 for first, 2 for second, etc, how they appear on the page
        product_full_xpath = f"{self.PRODUCT_XPATH_PRE}[{product_number + 1}]{self.PRODUCT_XPATH_POST}"
        add_to_cart_xpath = f"{self.PRODUCT_XPATH_PRE}[{product_number + 1}]{self.ADD_TO_CART_XPATH_POST}"

        product_element = (By.XPATH, product_full_xpath)
        add_to_cart_element = (By.XPATH, add_to_cart_xpath)

        hover_product = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(product_element))

        self.actions.move_to_element(hover_product).perform()
        time.sleep(2)

        add_to_cart_btn = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(add_to_cart_element))
        add_to_cart_btn.click()
        time.sleep(1)
        return self

    def click_continue_shopping_button_popup(self):
        continue_shopping_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CONTINUE_SHOPPING_BUTTON))
        continue_shopping_button.click()
        time.sleep(1)
        return self

    def click_view_cart_button_popup(self):
        view_cart_button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.VIEW_CART_BUTTON))
        view_cart_button.click()
        time.sleep(1)
        return self

    def hover_and_add_to_cart_and_view_cart(self, product_number):
        self.hover_and_add_to_cart(product_number)
        self.click_view_cart_button_popup()
        return self

    def hover_add_to_cart_and_continue_shopping(self, product_number):
        self.hover_and_add_to_cart(product_number)
        self.click_continue_shopping_button_popup()
        return self


    def verify_brands_are_visible(self):
        brands = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BRANDS_SECTION))

        self.driver.execute_script("arguments[0].scrollIntoView(true);", brands)

        # Optionally highlight the element for visual confirmation
        self.driver.execute_script("arguments[0].style.border='3px solid red'", brands)

        return brands.is_displayed()


    def click_brand(self, brand_number):
        brands = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.BRANDS_SECTION)).find_elements(By.TAG_NAME, 'a')

        brands[brand_number - 1].click()
        time.sleep(3)
        return self

    def user_is_navigated_to_brands_page(self):
        return True if self.driver.title != 'Automation Exercise - All Products' else False

    def number_or_searched_items(self):
        items = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.PRODUCT_LIST)).find_elements(By.CLASS_NAME, "col-sm-4")

        return len(items)

    def add_all_searched_products_to_cart(self):
        number_of_items = self.number_or_searched_items()
        for i in range(number_of_items):
            self.hover_add_to_cart_and_continue_shopping(i+1)
            time.sleep(1)

        return self

    def all_products_text_is_visible(self):
        product_text = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.ALL_PRODUCTS_TEXT))

        return product_text.is_displayed()

    def click_cart_button(self):
        button = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.visibility_of_element_located(self.CART_BUTTON))

        button.click()

        return self


