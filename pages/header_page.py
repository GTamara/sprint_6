import allure

from locators.dzen_locators import DzenLocatots
from pages.base_page import BasePage


class HeaderPage(BasePage):

    @allure.step('Кликнуть лого "Самокат"')
    def click_scooter_logo(self, scooter_logo_selector):
        self.click_element(scooter_logo_selector)

    @allure.step('Кликнуть лого "Яндекс"')
    def click_yandex_logo(self, yandex_logo_selector):
        self.click_element(yandex_logo_selector)

    @allure.step('Проверить, что произошел переход на https://dzen.ru')
    def is_yandex_dzen_resource(self):
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.find_element_with_wait(DzenLocatots.DZEN_SEARCH_ELEMENT)
        return 'https://dzen.ru' in self.driver.current_url