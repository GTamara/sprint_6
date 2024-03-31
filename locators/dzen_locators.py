from selenium.webdriver.common.by import By


class DzenLocatots:
    
    DZEN_LOGO = By.XPATH, '//a[@href="/"][@aria-label="Логотип Бренда"]'
    DZEN_SEARCH_ELEMENT = By.XPATH, '//form[contains(@class, "dzen-search")]'