import allure
from pages.base_page import BasePage
from locators.set_order_locators import SetOrderLocators


class SetOrderPage(BasePage):

    order_details_form_locators = SetOrderLocators.ORDER_DETAILS_FORM

    def set_order(self, data):
        # User details form filling
        with allure.step('Заполнить форму с данными клиента'):
            self.fill_text_field(
                SetOrderLocators.USER_DETAILS_FORM['NAME'],
                data['user_details_form_data']['name']
            )
            self.fill_text_field(
                SetOrderLocators.USER_DETAILS_FORM['SURNAME'],
                data['user_details_form_data']['surname']
            )
            self.fill_text_field(
                SetOrderLocators.USER_DETAILS_FORM['ADDRESS'],
                data['user_details_form_data']['address']
            )
            station_option_formatted_locator = self.format_locator(
                SetOrderLocators.USER_DETAILS_FORM['STATION_OPTION'],
                data['user_details_form_data']['station']
            )
            self.fill_dropdown(
                SetOrderLocators.USER_DETAILS_FORM['STATION'],
                station_option_formatted_locator,
            )
            self.fill_text_field(
                SetOrderLocators.USER_DETAILS_FORM['PHONE'], 
                data['user_details_form_data']['phone']
            )
        with allure.step('Кликнуть кнопку "Далее"'):
            self.click_element(SetOrderLocators.USER_DETAILS_FORM_NEXT_BUTTON)

        # Order details form filling
        with allure.step('Заполнить форму с деталями заказа'):
            self.fill_datepicker_manualy(
                SetOrderLocators.ORDER_DETAILS_FORM['DATE'],
                data['order_details_form_data']['date']
            )
            duration_option_formatted_locator = self.format_locator(
                SetOrderLocators.ORDER_DETAILS_FORM['DURATION_OPTION'],
                data['order_details_form_data']['duration']
            )
            self.fill_dropdown(
                SetOrderLocators.ORDER_DETAILS_FORM['DURATION'],
                duration_option_formatted_locator,
            )
            self.set_checkbox_value(
                SetOrderLocators.ORDER_DETAILS_FORM['COLOR_BLACK'],
                data['order_details_form_data']['color_black']
            )
            self.set_checkbox_value(
                SetOrderLocators.ORDER_DETAILS_FORM['COLOR_GRAY'],
                data['order_details_form_data']['color_gray']
            )
        with allure.step('Кликнуть кнопку подтверждения оформления заказа'):
            self.click_element(SetOrderLocators.ORDER_DETAILS_FORM_SUBMIT_BUTTON)
        with allure.step('Кликнуть кнопку подтверждения оформления заказа в модальном окне'):
            self.click_element(SetOrderLocators.ORDER_CONFIRMATION_MODAL_CONFIRM_BUTTON)

    @allure.step('Проверка наличия модального окна с номером заказа')
    def check_order_status_modal(self):
        return self.find_element_with_wait(
            SetOrderLocators.ORDER_STATUS_MODAL
        ).is_displayed()
    