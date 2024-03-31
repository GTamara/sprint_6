import allure
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.urls import Urls
from constants.constants import Constants
from pages.main_page import MainPage


class SharedMethods:

    @staticmethod
    def get_main_page(driver: WebDriver):
        driver.get(Urls.MAIN_PAGE_URL)

    @staticmethod
    def get_set_order_page(driver: WebDriver):
        driver.get(Urls.ORDER_PAGE_URL)
