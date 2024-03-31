from selenium.webdriver.common.by import By


class SetOrderLocators:

    USER_DETAILS_FORM = {
        'NAME': (By.XPATH, '//input[contains(@placeholder, "Имя")]'),
        'SURNAME': (By.XPATH, '//input[contains(@placeholder, "Фамилия")]'),
        'ADDRESS': (By.XPATH, '//input[contains(@placeholder, "Адрес")]'),
        'STATION': (By.XPATH, '//input[contains(@placeholder, "Станция метро")]'),
        'STATION_OPTION': (By.XPATH, '//button[contains(@class, "SelectOption")]/div[text()="{}"]'),
        'PHONE': (By.XPATH, '//input[contains(@placeholder, "Телефон")]'),
    }

    ORDER_DETAILS_FORM = {
        'DATE': (By.XPATH, '//input[contains(@placeholder, "Когда привезти самокат")]'),
        'DURATION': (By.XPATH, '//div[contains(text(), "Срок аренды")]/parent::*'),
        'DURATION_OPTION': (By.XPATH, '//div[contains(@class, "Dropdown-option")][text()="{}"]'),
        'COLOR_BLACK': (By.XPATH, '//label[text()="чёрный жемчуг"]/input[@type="checkbox"]'),
        'COLOR_GRAY': (By.XPATH, '//label[text()="серая безысходность"]/input[@type="checkbox"]'),
        'COMMENT': (By.XPATH, '//input[@placeholder="Комментарий для курьера"]'),
    }

    USER_DETAILS_FORM_NEXT_BUTTON = By.XPATH, '//button[text()="Далее"]'
    ORDER_DETAILS_FORM_SUBMIT_BUTTON = By.XPATH, '//div[contains(@class, "Order_Buttons")]/button[text()="Заказать"]'

    ORDER_CONFIRMATION_MODAL = By.XPATH, '//*[contains(@class, "Order_ModalHeader")][text()="Хотите оформить заказ?"]/parent::*'
    ORDER_CONFIRMATION_MODAL_CONFIRM_BUTTON = By.XPATH, '//*[contains(@class, "Order_Buttons")]/button[text()="Да"]'
    ORDER_STATUS_MODAL = By.XPATH, '//*[contains(@class, "Order_ModalHeader")][text()="Заказ оформлен"]/parent::*'
