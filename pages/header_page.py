import allure

from locators.header_locators import HeaderLocators
from locators.dzen_locators import DzenLocatots
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Кликнуть лого "Самокат"')
    def click_scooter_logo(self):
        self.click_element(
            HeaderLocators.HEADER_SCOOTER_LOGO
        )

    @allure.step('Кликнуть лого "Яндекс"')
    def click_yandex_logo(self):
        self.click_element(
            HeaderLocators.HEADER_YANDEX_LOGO
        )

    @allure.step('Проверить, что произошел переход на https://dzen.ru')
    def is_yandex_dzen_resource(self):
        self.switch_to_next_browser_tab()
        self.find_element_with_wait(DzenLocatots.DZEN_SEARCH_ELEMENT)
        return 'https://dzen.ru' in self.driver.current_url
    