import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Вводим Имя')
    def set_name(self, name):
        self.input_in_field(OrderPageLocators.NAME, name)

    @allure.step('Вводим Фамилию')
    def set_surname(self, surname):
        self.input_in_field(OrderPageLocators.SURNAME, surname)

    @allure.step('Вводим Адрес')
    def set_address(self, address):
        self.input_in_field(OrderPageLocators.ADDRESS, address)

    @allure.step('Кликаем на "Метро"')
    def click_metro_station(self):
        self.click_to_element(OrderPageLocators.METRO_STATION)

    @allure.step('Проверяем кликабельность кнопки Сокольники')
    def check_button_sokolniki(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.METRO_STATION_SOKOLNIKI)

    @allure.step('Кликаем по станции "Комсомольская"')
    def click_metro_sokolniki(self):
        self.click_to_element(OrderPageLocators.METRO_STATION_SOKOLNIKI)

    @allure.step('Вводим Телефон')
    def set_phone(self, phone):
        self.input_in_field(OrderPageLocators.PHONE, phone)

    @allure.step('Кликаем на кнопку "Далее"')
    def click_next(self):
        self.click_to_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Проверяем кликабельность кнопки "далее"')
    def check_button_next(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.BUTTON_NEXT)

    @allure.step('Проверяем кликабельность кнопки заказа')
    def check_button_order(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Кликаем по полю Дата')
    def click_date(self):
        self.click_to_element(OrderPageLocators.DATE)

    @allure.step('Кликаем по текущей дате')
    def click_today(self):
        self.click_to_element(OrderPageLocators.TODAY)

    @allure.step('Кликаем по срок аренды')
    def click_rental_period(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD)

    @allure.step('Кликаем по периоду аренды "Двое суток"')
    def click_rental_period_choose(self):
        self.click_to_element(OrderPageLocators.RENTAL_PERIOD_CHOOSE)

    @allure.step('Выбираем черный цвет')
    def click_black_color(self):
        self.click_to_element(OrderPageLocators.BLACK_COLOR)

    @allure.step('Проверяем кликабельность кнопки заказа')
    def check_button_order(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Кликаем на кнопку "Заказать"')
    def click_button_order(self):
        self.click_to_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step('Проверяем кликабельность кнопки "Да"')
    def check_button_yes_is_clickable(self):
        self.wait_for_element_to_be_clickable(OrderPageLocators.BUTTON_YES)

    @allure.step('Кликаем на кнопку "Да"')
    def click_button_yes(self):
        self.click_to_element(OrderPageLocators.BUTTON_YES)

    @allure.step('Проверяем видимость кнопки "Проверить статус"')
    def check_visibility_of_button_status(self):
        self.find_element(OrderPageLocators.BUTTON_STATUS)

    @allure.step('Получаем текст кнопки "Проверить статус"')
    def get_text_on_the_button_status(self):
        return self.get_text_element(OrderPageLocators.BUTTON_STATUS)

    @allure.step('Заполнение данных на форме "Для кого самокат"')
    def set_data_order(self, name, surname, address, phone):
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.click_metro_station()
        self.check_button_sokolniki()
        self.click_metro_sokolniki()
        self.set_phone(phone)

    @allure.step('Заполнение данных на форме "Про аренду"')
    def set_data_order_about_rent(self):
        self.check_button_order()
        self.click_date()
        self.click_today()
        self.click_rental_period()
        self.click_rental_period_choose()
        self.click_black_color()
        self.check_button_order()
        self.click_button_order()
        self.check_button_yes_is_clickable()
        self.click_button_yes()

    @allure.step('Проверяем кликабельность кнопки далее и кликаем"')
    def check_and_сlick_button_next(self):
        self.check_button_next()
        self.click_next()
