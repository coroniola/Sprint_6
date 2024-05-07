import allure
from pages.main_page import MainPage
from settings import Urls




class TestClickLogo:
    @allure.title('Проверяем переход на главную при клике на логотип Самокат')

    def test_click_logo_scooter_to_general_page(self, driver, click_cookie):
        main_page = MainPage(driver)
        main_page.check_header_button_order_is_clickable()
        main_page.click_header_order_button()
        main_page.click_scooter_logo()
        current_url = main_page.get_current_url()
        assert Urls.start_page in current_url


    @allure.title('Проверяем переход на Дзен при клике на логотип Yandex')
    def test_click_logo_ya_to_dzen_page(self, driver, click_cookie):
        main_page = MainPage(driver)
        main_page.click_to_yandex_logo()
        main_page.swith_to_new_tab()
        main_page.wait_for_load_url(Urls.dzen_url)
        assert Urls.dzen_url in main_page.get_current_url()
