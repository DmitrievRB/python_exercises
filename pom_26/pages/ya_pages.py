from pages.base_page import *
from selenium.webdriver.common.by import By


class YaSearchLocators:
    LOCATOR_YA_SEARCH_FILD = (By.ID, "text")
    LOCATOR_YA_SEARCH_BUTTON = (By.XPATH, "//button[contains(text(),'Найти')]")


class SearchHelper(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_FILD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_search_button(self):
        return self.find_element(YaSearchLocators.LOCATOR_YA_SEARCH_BUTTON, timeout=3).click()
