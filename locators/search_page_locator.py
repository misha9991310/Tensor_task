from selenium.webdriver.common.by import By


class SearchPageLocators:
    SEARCH_ROW = (By.XPATH, '//input[@name="text"]')
    SEGGEST = (By.XPATH, '//li[@data-index="0"]')
    LINK = (By.CSS_SELECTOR, '.link.path__item.link.organic__greenurl > b')
    SEARCH_RESULT = (By.XPATH, '//*[@id="search-result"]')


class ImagePageLocators:
    ALL_SERVICES = (By.XPATH, '//a[@title="Все сервисы"]')
    IMAGES = (By.XPATH, '//a[@aria-label="Картинки"]')
    FIRST_CATEGORY_IMAGE = (By.XPATH, '//div[@class="PopularRequestList-Item PopularRequestList-Item_pos_0"]')
    SEARCH_ROW = (By.XPATH, '//input[@name="text"]')
    OPEN_IMAGE = (By.CSS_SELECTOR, '.MediaViewer-View.MediaViewer_theme_fiji-View > div > img')
    BUTTON_PREV = (By.CSS_SELECTOR, '.MediaViewer-ButtonPrev.MediaViewer_theme_fiji-ButtonPrev > i')
    BUTTON_NEXT = (By.CSS_SELECTOR, '.MediaViewer-ButtonNext.MediaViewer_theme_fiji-ButtonNext > i')
    FIRST_IMAGE = (By.CSS_SELECTOR, '.serp-item_pos_0.justifier__item.i-bem.justifier__item_first')