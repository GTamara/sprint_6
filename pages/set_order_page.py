import allure
from pages.base_page import BasePage


class SetOrderPage(BasePage):

    def set_order(
        self,
        user_details_locators: dict[str, tuple[str, str]],
        order_details_locators: dict[str, tuple[str, str]],
        next_btn_locator: tuple[str, str],
        submit_btn_locator: tuple[str, str],
        confirm_btn_locator: tuple[str, str], 
        data
    ):
        # User details form filling
        with allure.step('Заполнить форму с данными клиента'):
            self.fill_text_field(
                user_details_locators['NAME'],
                data['user_details_form_data']['name']
            )
            self.fill_text_field(
                user_details_locators['SURNAME'],
                data['user_details_form_data']['surname']
            )
            self.fill_text_field(
                user_details_locators['ADDRESS'],
                data['user_details_form_data']['address']
            )
            station_option_formatted_locator = self.format_locator(
                user_details_locators['STATION_OPTION'],
                data['user_details_form_data']['station']
            )
            self.fill_dropdown(
                user_details_locators['STATION'],
                station_option_formatted_locator,
            )
            self.fill_text_field(user_details_locators['PHONE'], data['user_details_form_data']['phone'])
        with allure.step('Кликнуть кнопку "Далее"'):
            self.click_element(next_btn_locator)

        # Order details form filling
        with allure.step('Заполнить форму с деталями заказа'):
            self.fill_datepicker_manualy(
                order_details_locators['DATE'],
                data['order_details_form_data']['date']
            )
            duration_option_formatted_locator = self.format_locator(
                order_details_locators['DURATION_OPTION'],
                data['order_details_form_data']['duration']
            )
            self.fill_dropdown(
                order_details_locators['DURATION'],
                duration_option_formatted_locator,
            )
            self.set_checkbox_value(
                order_details_locators['COLOR_BLACK'],
                data['order_details_form_data']['color_black']
            )
            self.set_checkbox_value(
                order_details_locators['COLOR_GRAY'],
                data['order_details_form_data']['color_gray']
            )
        with allure.step('Кликнуть кнопку подтверждения оформления заказа'):
            self.click_element(submit_btn_locator)
        with allure.step('Кликнуть кнопку подтверждения оформления заказа в модальном окне'):
            self.click_element(confirm_btn_locator)

    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self, locator):
        self.click_element(locator)

    @allure.step('Проверка наличия модального окна с номером заказа')
    def check_order_status_modal(self, locator):
        return bool(
            self.find_element_with_wait(locator)
        )
