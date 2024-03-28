import allure
import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from pages.set_order_page import SetOrderPage
from data.set_order_data import set_order_data
from shared_methods import SharedMethods


class TestSetOrderPage():

    @allure.title('Оформление заказа. Успешный сценарий')
    @allure.description('Проверить, что клик по кнопке "Заказать" ведет на страницу оформления заказа. '
                        'Проверяется успешный сценарий оформления заказа')
    @pytest.mark.parametrize('order_btn_locator', [
        HeaderLocators.HEADER_ORDER_BUTTON,
        MainPageLocators.ROAD_MAP_ORDER_BUTTON,
    ])
    @pytest.mark.parametrize('data', set_order_data)
    def test_set_order_by_road_map_btn_success(self, driver: WebDriver, order_btn_locator, data):
        SharedMethods.get_main_page(driver)
        set_order_page = SetOrderPage(driver)
        set_order_page.scroll_to_element(order_btn_locator)
        set_order_page.click_element(order_btn_locator)
        set_order_page.set_order(data)
        assert set_order_page.check_order_status_modal()
        