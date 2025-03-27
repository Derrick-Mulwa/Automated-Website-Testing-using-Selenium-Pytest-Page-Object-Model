import pytest
from selenium import webdriver
import os
from utilities.read_properties import ReadConfig

@pytest.fixture()
def setup():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--log-level=4")

    options.page_load_strategy = 'eager'
    
    prefs = {
        "download.default_directory": ReadConfig.get_downloads_filepath(),
        "download.prompt_for_download": False,
        'autofill.profile_enabled': False
    }
    options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=options)
    
    driver.set_network_conditions(
        offline=False,
        latency=5,
        download_throughput=10 * 1024 * 1024 / 8,
        upload_throughput=10 * 1024 * 1024 / 8
    )

    driver.set_page_load_timeout(1000)

    yield driver
    driver.quit()
