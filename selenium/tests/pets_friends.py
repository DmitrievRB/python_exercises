import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_pet_friens_login(web_driver):
    web_driver.get("https://petfriends.skillfactory.ru/")
    reg=web_driver.find_element(By.CLASS_NAME,"btn.btn-success")
    # reg.send_keys(Keys.RETURN)
    time.sleep(2)