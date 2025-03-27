import configparser
import ast
import os

config = configparser.RawConfigParser()
config.read('.\\configurations\\configurations.ini')

class ReadConfig:
    @staticmethod
    def get_base_url():
        return config.get('USER_DATA', 'BASE_URL')

    @staticmethod
    def get_gender():
        return config.get('USER_DATA', 'gender')

    @staticmethod
    def get_name():
        return config.get('USER_DATA', 'name')

    @staticmethod
    def get_email():
        return config.get('USER_DATA', 'email')

    @staticmethod
    def get_password():
        return config.get('USER_DATA', 'password')

    @staticmethod
    def get_dob_day():
        return config.get('USER_DATA', 'dob_day')

    @staticmethod
    def get_dob_month():
        return config.get('USER_DATA', 'dob_month')

    @staticmethod
    def get_dob_year():
        return config.get('USER_DATA', 'dob_year')

    @staticmethod
    def get_first_name():
        return config.get('USER_DATA', 'first_name')

    @staticmethod
    def get_last_name():
        return config.get('USER_DATA', 'last_name')

    @staticmethod
    def get_company():
        return config.get('USER_DATA', 'company')

    @staticmethod
    def get_address1():
        return config.get('USER_DATA', 'address1')

    @staticmethod
    def get_address2():
        return config.get('USER_DATA', 'address2')

    @staticmethod
    def get_country():
        return config.get('USER_DATA', 'country')

    @staticmethod
    def get_state():
        return config.get('USER_DATA', 'state')

    @staticmethod
    def get_city():
        return config.get('USER_DATA', 'city')

    @staticmethod
    def get_zipcode():
        return config.get('USER_DATA', 'zipcode')

    @staticmethod
    def get_mobile_number():
        return config.get('USER_DATA', 'mobile_number')

    @staticmethod
    def get_correct_email():
        return config.get('USER_DATA', 'correct_email')

    @staticmethod
    def get_correct_password():
        return config.get('USER_DATA', 'correct_password')

    @staticmethod
    def get_incorrect_email():
        return config.get('USER_DATA', 'incorrect_email')

    @staticmethod
    def get_incorrect_password():
        return config.get('USER_DATA', 'incorrect_password')

    @staticmethod
    def get_timeout_value():
        return config.get('SETTINGS', 'TIMEOUT')

    @staticmethod
    def get_contact_subject():
        return config.get('CONTACT_US', 'subject')

    @staticmethod
    def get_contact_message():
        return config.get('CONTACT_US', 'message')

    @staticmethod
    def get_contact_us_filepath():
        return os.path.abspath(config.get('CONTACT_US', 'file'))

    @staticmethod
    def get_downloads_filepath():
        return os.path.abspath(config.get('SETTINGS', 'downloads_path'))

    @staticmethod
    def get_search_text():
        return config.get('ALL_PRODUCTS', 'search_text')

    @staticmethod
    def get_first_two_product_data():
        products_str = config.get('first_two_products', 'products')
        products_list = ast.literal_eval(products_str)
        return products_list

    @staticmethod
    def get_card_number():
        return config.get('CARD_DETAILS', 'Card_Number')

    @staticmethod
    def get_cvc():
        return config.get('CARD_DETAILS', 'CVC')

    @staticmethod
    def get_expiration_month():
        return config.get('CARD_DETAILS', 'Expiration_Month')

    @staticmethod
    def get_expiration_year():
        return config.get('CARD_DETAILS', 'Expiration_Year')

