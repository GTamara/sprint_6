import allure
import pytest
from selenium.webdriver.firefox.webdriver import WebDriver

from locators.header_locators import HeaderLocators
from locators.main_page_locators import MainPageLocators
from locators.set_order_locators import SetOrderLocators
from pages.set_order_page import SetOrderPage
from data.set_order_data import set_order_data
from shared_methods import SharedMethods


class TestSetOrderPage():

    user_details_form_locators = SetOrderLocators.USER_DETAILS_FORM
    order_details_form_locators = SetOrderLocators.ORDER_DETAILS_FORM

    @allure.title('Оформление заказа. Кнопка "Заказать" в шапке. Успешный сценарий')
    @allure.description('Проверить, что клик по кнопке "Заказать" в шапке сайта ведет на страницу оформления заказа. '
                        'Проверяется успешный сценарий ')
    @pytest.mark.parametrize(
        'data',
        set_order_data
    )
    def test_set_order_by_header_btn_success(self, driver: WebDriver, data):
        SharedMethods.get_main_page(driver)
        set_order_page = SetOrderPage(driver)
        set_order_page.click_order_button(
            HeaderLocators.HEADER_ORDER_BUTTON
        )
        set_order_page.set_order(
            self.user_details_form_locators,
            self.order_details_form_locators,
            SetOrderLocators.USER_DETAILS_FORM_NEXT_BUTTON,
            SetOrderLocators.ORDER_DETAILS_FORM_SUBMIT_BUTTON,
            SetOrderLocators.ORDER_CONFIRMATION_MODAL_CONFIRM_BUTTON,
            data
        )
        assert set_order_page.check_order_status_modal(SetOrderLocators.ORDER_STATUS_MODAL)

    @allure.title('Оформление заказа. Кнопка "Заказать" в разделе "Как это работает". Успешный сценарий')
    @allure.description('Проверить, что клик по кнопке "Заказать" в разделе "Как это работает" ведет на страницу оформления заказа. '
                        'Проверяется успешный сценарий ')
    @pytest.mark.parametrize(
        'data',
        set_order_data
    )
    def test_set_order_by_road_map_btn_success(self, driver: WebDriver, data):
        SharedMethods.get_main_page(driver)
        set_order_page = SetOrderPage(driver)
        set_order_page.scroll_to_element(MainPageLocators.ROAD_MAP_ORDER_BUTTON)
        set_order_page.click_order_button(
            MainPageLocators.ROAD_MAP_ORDER_BUTTON
        )
        set_order_page.set_order(
            self.user_details_form_locators,
            self.order_details_form_locators,
            SetOrderLocators.USER_DETAILS_FORM_NEXT_BUTTON,
            SetOrderLocators.ORDER_DETAILS_FORM_SUBMIT_BUTTON,
            SetOrderLocators.ORDER_CONFIRMATION_MODAL_CONFIRM_BUTTON,
            data
        )
        assert set_order_page.check_order_status_modal(SetOrderLocators.ORDER_STATUS_MODAL)