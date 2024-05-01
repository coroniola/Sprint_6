
import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Кликаем на элемент')
    def click_to_element(self, element):
        self.driver.find_element(*element).click()

    @allure.step('Ждем пока элемент прогрузится и станет кликабелен')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(
            expected_conditions.element_to_be_clickable(locator))

    @allure.step('Заполняем элемент')
    def input_in_field(self, element, keys):
        self.driver.find_element(*element).send_keys(keys)

    @allure.step('ищем элемент на странице')
    def find_element(self, locator, timeout=5):
        return WebDriverWait(self.driver, timeout).until(
            expected_conditions.visibility_of_element_located(locator))

    @allure.step('Получаем текст элемента')
    def get_text_element(self, locator):
        return self.driver.find_element(*locator).text


