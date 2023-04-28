from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class YaSearchPageLocators:
    LOCATOR_YANDEX_NAVI_BAR = (By.CLASS_NAME, "service__name")


class SearchPageHelper(BasePage):
    def check_navi_bar(self):
        all_list = self.find_elements(YaSearchPageLocators.LOCATOR_YANDEX_NAVI_BAR)
        navi = [x.text for x in all_list]
        # print(navi)
        return navi
