from selenium.webdriver.common.by import By


class MainPageLocators:

    ACCEPT_COOKIES_BUTTON = [By.ID, 'rcc-confirm-button'] #кнопка принятия кук
    QUESTION_LOC = [By.ID, 'accordion__heading-{}'] # заголовок вопроса в разворачивающемся меню
    ANSWER_LOC = [By.ID, 'accordion__panel-{}'] # заголовок ответа в разворачивающемся меню
    HEADER_ORDER_BUTTON = [By.XPATH, '//div[ contains(@class, "Header")]/button[ text()="Заказать" ]'] # кнопка Заказать в шапке
    BODY_ORDER_BUTTON = [By.CLASS_NAME, "Button_Button__ra12g Button_Middle__1CSJM"] # кнопка Заказать в теле страницы
