# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import pytest
#
# options = Options()
# options.add_argument("--no-sandbox")
# # options.add_argument("--headless")
# options.add_argument("--disable-gpu")
# options.add_argument("--windows-size=800,600")
# options.add_argument("--disable-dev-shw-usage")
# #chrome_options.add_argument("--disable-extensions")
#
# @pytest.fixture(autouse=True)
# def web_driver():
#     driver = webdriver.Chrome(options=options)
#     # start_url = "https://petfriends.skillfactory.ru/"
#
#     # driver.get(start_url)
#     # print(driver.page_source.encode("utf-8"))
#     # driver.quit()
#     return driver