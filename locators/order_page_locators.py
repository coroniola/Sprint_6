from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME = [By.XPATH, '//input[@placeholder="* Имя"]'] # Поле Имя в форме заказа
    SURNAME = [By.XPATH, '//input[@placeholder="* Фамилия"]'] # Поле Фамилия в форме заказа
    ADDRESS = [By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]'] #  Поле Адрес в форме заказа
    METRO_STATION = [By.XPATH, '//input[@placeholder="* Станция метро"]']  # Поле метро в форме заказа
    METRO_STATION_SOKOLNIKI = [By.XPATH, f'//div[text()= "Сокольники"]'] # Станция метро Сокольники
    PHONE = [By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]'] # Поле Телефон в форме заказа
    DATE = [By.XPATH, '//input[@placeholder="* Когда привезти самокат"]'] # Календарь с выбором даты в форме заказа
    TODAY = [By.CLASS_NAME, 'react-datepicker__day--today'] #  Дата в календаре форме заказа
    RENTAL_PERIOD = [By.CLASS_NAME, 'Dropdown-placeholder'] # Поле срок аренды в форме заказа
    RENTAL_PERIOD_CHOOSE = [By.XPATH, '//div[@class = "Dropdown-option" and text()="двое суток"]'] #  Выбор срока аренды в выпадающей форме
    BLACK_COLOR = [By.ID, 'black'] # черный цвет
    BUTTON_NEXT = [By.XPATH, '//div[@class="Order_NextButton__1_rCA"]/button[text()= "Далее"]'] # кнопка далее
    BUTTON_ORDER = [By.XPATH, '//div[@class="Order_Buttons__1xGrp"]/button[text()= "Заказать"]'] # кнопка Заказать
    BUTTON_YES = [By.XPATH, './/button[text()= "Да"]'] # кнопка Да
    BUTTON_STATUS = [By.XPATH, './/button[text()= "Посмотреть статус"]'] # Кнопка статуса
