import allure
import pytest
from data.main_page_data import important_things_questions
from shared_methods import SharedMethods
from pages.main_page import MainPage


class TestMainPage:

    @allure.title('Раздел "Вопросы о важном". Проверка содержания вопросов и ответов.')
    @allure.description('Проверить, что раздел содержит правильные вопросы и ответа, и они соответствуют один другу')
    @pytest.mark.parametrize(
        'item',
        important_things_questions
    )
    def test_check_important_things_answer_and_question(self, driver, item):
        main_page = MainPage(driver)
        SharedMethods.get_main_page(driver)
        num = important_things_questions.index(item)
        question_text = main_page.find_important_things_question(num)
        main_page.scroll_to_question(num)
        main_page.click_question(num)

        answer_text = main_page.find_important_things_answer(num)
        assert question_text == item['question']
        assert answer_text == item['answer']

