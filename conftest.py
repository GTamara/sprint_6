import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions


@pytest.fixture(scope="function")
def driver():
    options = FirefoxOptions()
    options.add_argument('--window-size=1920, 1080')
    with allure.step('Открыть окно Firefox браузера'):
        driver = webdriver.Firefox(options=options)
    yield driver
    with allure.step('Закрыть окно Firefox браузера'):
        driver.quit()

