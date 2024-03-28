import allure

from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def find_important_things_entity(self, locator: tuple[str, str], num):
        formatted_locator = self.format_locator(
            locator, 
            num
        )
        return self.find_element_with_wait(formatted_locator).text
    
    @allure.step('Найти вопрос по номеру и получить его текст')
    def find_important_things_question(self, num):
        return self.find_important_things_entity(MainPageLocators.IMPORTANT_THINGS_QUESTION, num)

    @allure.step('Найти ответ по номеру и получить его текст')
    def find_important_things_answer(self, num):
        return self.find_important_things_entity(MainPageLocators.IMPORTANT_THINGS_ANSWER, num)

    @allure.step('Кликнуть вопрос с заданным номером')
    def click_question(self, num: int):
        formatted_locator = self.format_locator(
            MainPageLocators.IMPORTANT_THINGS_QUESTION, 
            num
        )
        return self.click_element(formatted_locator)

    @allure.step('Проскролить страницу к вопросу с заданным номером')
    def scroll_to_question(self, num):
        formatted_locator = self.format_locator(
            MainPageLocators.IMPORTANT_THINGS_QUESTION, 
            num
        )
        self.scroll_to_element(formatted_locator)

    @allure.step('Получить содержимое тега заголовка страницы')
    def get_main_page_heading_content(self):
        return self.find_element_with_wait(MainPageLocators.MAIN_PAGE_HEADING).text


    @allure.step('Клик по кнопке "Заказать"')
    def click_order_button(self):
        self.click_element(MainPageLocators.ROAD_MAP_ORDER_BUTTON)