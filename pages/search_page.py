from selenium.webdriver import Keys

from pages.base_page import BasePage
from locators.search_page_locator import SearchPageLocators as Locators


class SearchPage(BasePage):

    def search_and_submit(self):
        search_row = self.element_is_visible(Locators.SEARCH_ROW)
        search_row.send_keys('Тензор')

    def enter_click(self):
        search_row = self.element_is_visible(Locators.SEARCH_ROW)
        search_row.send_keys(Keys.ENTER)

    def check_table_suggest(self):
        seggest = self.element_is_visible(Locators.SEGGEST)
        return seggest.is_displayed()

    def check_search(self):
        resul_search = self.element_is_visible(Locators.SEARCH_RESULT)
        return resul_search.is_displayed()

    def check_first_link(self):
        link = self.driver.find_element(*Locators.LINK).text
        return link


