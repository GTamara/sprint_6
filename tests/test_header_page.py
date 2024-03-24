import allure

from helper_functions import HelperFunctions
from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from pages.header_page import HeaderPage
from shared_methods import SharedMethods


class TestHeaderPage:

    @allure.title('Проверить, что клик по логотипу "Самокат" ведет на главную страницу')
    def test_click_scooter_logo_directs_to_main_page(self, driver):
        SharedMethods.get_set_order_page(driver)
        header_page = HeaderPage(driver)
        scooter_logo_locator = HeaderLocators.HEADER_SCOOTER_LOGO
        header_page.click_scooter_logo(scooter_logo_locator)
        main_page_heading_text = HelperFunctions.get_text_from_raw_html(
            driver.find_element(*MainPageLocators.MAIN_PAGE_HEADING).text
        )
        assert 'самокат на пару дней' in main_page_heading_text.lower()

    @allure.title('Проверить, что клик по логотипу "Яндекс" ведет на главную страницу Яндекс Дзен')
    def test_click_yandex_logo_directs_to_dzen_page(self, driver):
        SharedMethods.get_main_page(driver)
        header_page = HeaderPage(driver)
        yandex_logo_locator = HeaderLocators.HEADER_YANDEX_LOGO
        header_page.click_yandex_logo(yandex_logo_locator)
        header_page.is_yandex_dzen_resource()
        assert header_page.is_yandex_dzen_resource()

