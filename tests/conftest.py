import time

import pytest
from selenium import webdriver
from settings import Urls
from pages.main_page import MainPage


@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(Urls.start_page)
    yield driver
    driver.quit()

@pytest.fixture
def click_cookie(driver):
    main_page = MainPage(driver)
    main_page.click_cookies_button()