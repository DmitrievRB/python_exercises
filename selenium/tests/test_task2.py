from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from selenium.webdriver.firefox.options import Options as FirefoxOptions
# from selenium.webdriver.edge.options import Options as EdgeOptions
import pytest

@pytest.fixture(params=["firefox","chrome","edge"],scope="function")
def init_driver(request):
    # Тест прогоняем по очереди в указанных браузерах
    if request.param == ("firefox"):
        firefox_options = webdriver.FirefoxOptions()
        web_driver = webdriver.Firefox(options=firefox_options)
    if request.param == ("chrome"):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-gpu")
        web_driver = webdriver.Chrome(options=chrome_options)

    if request.param == ("edge"):
        edge_options = webdriver.EdgeOptions()
        web_driver = webdriver.Edge(options=edge_options)
    yield web_driver
    web_driver.close()

@pytest.mark.usefixtures("init_driver")
def test_login(init_driver):
    # Запускаем тестируемый сайт
    init_driver.get("https://petfriends.skillfactory.ru/")
    # Находим тестируемый элемент(в имени класса меняем пробелы на точки)
    elem=init_driver.find_element(By.CLASS_NAME,"btn.btn-success")
    # Печатаем об успешном тестировании сайта
    print("successfuly access {}".format("petfriends.skillfactory.ru"))


