from selenium.webdriver.common.by import By


class HeaderLocators:
    HEADER_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Header_Header")]//button[text()="Заказать"]'
    HEADER_SCOOTER_LOGO = By.XPATH, '//img[@alt="Scooter"]/parent::a'
    HEADER_YANDEX_LOGO = By.XPATH, '//img[@alt="Yandex"]/parent::a'
