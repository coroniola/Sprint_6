import pytest
import allure
import settings
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrder:

    @allure.title('Проверка позитивного создания заказа при помощи кнопки в шапке')
    @allure.description('При успешном заказе появляется окно с кнопкой "Проверить статус"')
    @pytest.mark.parametrize('name, surname, address, phone', [*settings.RegistrationData.order_data])
    def test_positive_order(self, driver, click_cookie, name, surname, address, phone):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.click_header_order_button()
        order_page.set_data_order(name, surname, address, phone)
        order_page.check_and_lick_check_button_next()
        order_page.set_data_order_about_rent()
        order_page.check_visibility_of_button_status()
        text_in_button = order_page.get_text_on_the_button_status()
        assert text_in_button == 'Посмотреть статус'

