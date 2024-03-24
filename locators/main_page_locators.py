from selenium.webdriver.common.by import By


class MainPageLocators:

    MAIN_PAGE_HEADING = By.XPATH, '//div[contains(@class, "Home_Header")]'

    IMPORTANT_THINGS_QUESTION = By.CSS_SELECTOR, '#accordion__heading-{}'
    IMPORTANT_THINGS_ANSWER = By.CSS_SELECTOR, '#accordion__panel-{}'

    ROAD_MAP_ORDER_BUTTON = By.XPATH, '//div[contains(@class, "Home_RoadMap")]//button[text()="Заказать"]'
