from selenium.webdriver import Keys
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from constants.constants import Constants


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element_with_wait(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            expected_conditions.visibility_of_element_located(locator)
        )
        return self.driver.find_element(*locator)

    def click_element(self, locator: tuple[str, str]):
        WebDriverWait(self.driver, Constants.TIMEOUT).until(
            expected_conditions.element_to_be_clickable(locator)
        )
        self.driver.find_element(*locator).click()

    def scroll_to_element(self, locator: tuple[str, str]):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @staticmethod
    def format_locator(
            locator: tuple[str, str],
            num: int | str
    ) -> tuple[str, str]:
        method, selector = locator
        formatted_locator: str = selector.format(num)
        return method, formatted_locator

    def get_text_node(self, locator: tuple[str, str]):
        return self.find_element_with_wait(locator).text

    def fill_text_field(self, locator: tuple[str, str], value):
        return self.find_element_with_wait(locator).send_keys(value)
    
    def fill_dropdown(
        self, 
        dropdown_locator: tuple[str, str], 
        option_locator: tuple[str, str]
    ):
        self.click_element(dropdown_locator)
        self.click_element(option_locator)

    def fill_datepicker_manualy(
        self,
        locator: tuple[str, str], 
        value
    ):
        self.fill_text_field(locator, value)
        self.driver.find_element(*locator).send_keys(Keys.ESCAPE)

    def set_checkbox_value(self, locator, checked):
        checkbox = self.find_element_with_wait(locator)
        current_value = checkbox.get_attribute('checked')
        if bool(current_value) != checked:
            checkbox.click()

