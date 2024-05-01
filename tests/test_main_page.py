
import pytest
from pages.main_page import MainPage
from settings import FAQ
import allure


class TestAccordionReplies:

    @allure.title('Проверка соответствия вопроса и ответа в разделе вопросов и ответов')
    @pytest.mark.parametrize('question_number, expected_answer', FAQ.Answers)
    def test_accordion_questions(self, driver, click_cookie, question_number, expected_answer):
        self.driver = driver
        main_page = MainPage(self.driver)
        main_page.click_to_question(question_number)
        important_reply = main_page.get_answer(question_number)
        assert important_reply == expected_answer