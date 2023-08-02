from pages.base_page import BasePage
from locators.search_page_locator import ImagePageLocators as Locators



class ImagePage(BasePage):

    def search_imnge(self):
        search_row = self.element_is_visible(Locators.SEARCH_ROW)
        search_row.click()
        all_services = self.driver.find_element(*Locators.ALL_SERVICES)
        all_services.click()
        image = self.driver.find_element(*Locators.IMAGES)
        image.click()
        self.driver.switch_to.window(self.driver.window_handles[1])

    def check_url(self):
        url = self.driver.current_url
        return url

    def first_category_image(self):
        first_image = self.element_is_visible(Locators.FIRST_CATEGORY_IMAGE)
        category_name = first_image.text
        first_image.click()
        search_row = self.driver.find_element(*Locators.SEARCH_ROW).get_attribute("value")
        return category_name, search_row

    def open_first_image(self):

        try:
            first_image = self.element_is_visible(Locators.FIRST_IMAGE)
            first_image.click()
            return True
        except:
            return False

    def next_image(self):
        id_image1 = self.driver.find_element(*Locators.OPEN_IMAGE).get_attribute('src')
        next_button = self.driver.find_element(*Locators.BUTTON_NEXT)
        next_button.click()
        id_image2 = self.driver.find_element(*Locators.OPEN_IMAGE).get_attribute('src')
        return id_image1, id_image2

    def prev_image(self):
        next_button = self.driver.find_element(*Locators.BUTTON_PREV)
        next_button.click()
        id_image = self.driver.find_element(*Locators.OPEN_IMAGE).get_attribute('src')
        return id_image
