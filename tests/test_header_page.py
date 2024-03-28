import allure

from helper_functions import HelperFunctions
from pages.header_page import HeaderPage
from pages.main_page import MainPage
from shared_methods import SharedMethods


class TestHeaderPage:

    @allure.title('Проверить, что клик по логотипу "Самокат" ведет на главную страницу')
    def test_click_scooter_logo_directs_to_main_page(self, driver):
        SharedMethods.get_set_order_page(driver)
        header_page = HeaderPage(driver)
        header_page.click_scooter_logo()
        main_page = MainPage(driver)
        main_page_heading_content = main_page.get_main_page_heading_content()
        main_page_heading_text = HelperFunctions.get_text_from_raw_html(
            main_page_heading_content
        )
        assert 'самокат на пару дней' in main_page_heading_text.lower()

    @allure.title('Проверить, что клик по логотипу "Яндекс" ведет на главную страницу Яндекс Дзен')
    def test_click_yandex_logo_directs_to_dzen_page(self, driver):
        SharedMethods.get_main_page(driver)
        header_page = HeaderPage(driver)
        header_page.click_yandex_logo()
        assert header_page.is_yandex_dzen_resource()

