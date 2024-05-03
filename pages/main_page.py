from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
import allure

from locators.general_locators import GeneralLocators

class MainPage(BasePage):

    @allure.step('Кликаем по кнопке принятия куки')
    def click_cookies_button(self):
        self.click_to_element(MainPageLocators.ACCEPT_COOKIES_BUTTON)

    @allure.step('Кликаем на вопрос')
    def click_to_question(self, number):
        method, locator = MainPageLocators.QUESTION_LOC
        locator = locator.format(number)
        element = [method, locator]
        self.click_to_element(element)

    @allure.step('Получаем ответ')
    def get_answer(self, number):
        method, locator = MainPageLocators.ANSWER_LOC
        locator = locator.format(number)
        element = self.find_element((method, locator))
        return element.text

    @allure.step('Кликаем на кнопку заказа в шапке сайта')
    def click_header_order_button(self):
        self.click_to_element(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Кликаем на кнопку заказа в середине страницы')
    def click_body_order_button(self):
        self.click_to_element(MainPageLocators.BODY_ORDER_BUTTON)

    @allure.step('Проверяем доступность кнопки Заказать в шапке')
    def check_header_button_order_is_clickable(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.HEADER_ORDER_BUTTON)

    @allure.step('Проверяем доступность кнопки заказать в теле страницы')
    def check_body_button_order_is_clickable(self):
        self.wait_for_element_to_be_clickable(MainPageLocators.BODY_ORDER_BUTTON)

    @allure.step('Нажимаем на кнопку "заказать" в конце страницы')
    def click_body_ordering_button(self):
        self.click_to_element(MainPageLocators.BODY_ORDER_BUTTON)


    @allure.step('Кликаем по логотипу самоката')
    def click_scooter_logo(self):
        self.click_to_element(GeneralLocators.LOGO_SCOOTER)

    @allure.step('Кликаем на лого Яндекс и переходим на страницу дзен в новом окне')
    def click_to_yandex_logo(self):
        self.click_to_element(GeneralLocators.LOGO_YANDEX)

