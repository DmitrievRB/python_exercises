from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_argument("--no-sandbox")
options.add_argument("--disable-gpu")
options.add_argument("--windows-size=800,600")
options.add_argument("--disable-dev-shw-usage")

driver = webdriver.Chrome(options=options)
driver.get("https://petfriends.skillfactory.ru/")
assert "PetFriends" in driver.title
reg = driver.find_element(By.CLASS_NAME,"btn.btn-success")
reg.click()
sleep(3)
assert "PetFriends: New User" in driver.title
new_window = driver.switch_to.new_window()
driver.get("https://petfriends.skillfactory.ru/apidocs/#/")
assert "Flasgger" in driver.title
sleep(3)
driver.switch_to.window(driver.window_handles[0])
sleep(3)
driver.refresh()
driver.close()
driver.quit()
