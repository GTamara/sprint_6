import allure

from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Найти сущность по номеру и получить ее текст')
    def find_important_things_entity(self, locator, num):
        formatted_locator = self.format_locator(locator, num)
        return self.find_element_with_wait(formatted_locator).text

    @allure.step('Кликнуть вопрос')
    def click_question(self, locator: tuple[str, str], num: int):
        formatted_locator = self.format_locator(locator, num)
        return self.click_element(formatted_locator)

    @allure.step('Проскролить страницу к вопросу с заданным номером')
    def scroll_to_question(self, locator, num):
        formatted_locator = self.format_locator(locator, num)
        self.scroll_to_element(formatted_locator)




