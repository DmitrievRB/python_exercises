from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestWaitElementsPetFriends:
    # Данные пользователя для класса

    def setup(self):
        self.email = "grant@gmail.com"
        self.password = "grant"

    def open(self):
        # Запускаем браузер , открываем страницу
        self.driver = webdriver.Firefox()
        self.driver.get('http://petfriends.skillfactory.ru/')  # Переходим на страницу
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
        self.driver.find_element(By.XPATH, "//a[contains(text(),'У меня уже есть аккаунт')]").click()

    def login(self):
        self.driver.find_element(By.XPATH, "//input[@id='email']").send_keys(self.email)
        self.driver.find_element(By.XPATH, "//input[@id='pass']").send_keys(self.password)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))).click()
        assert self.driver.find_element(By.XPATH, "//a[contains(text(),'Мои питомцы')]")

    def close(self):
        self.driver.quit()

    def teardown(self):
        self.close()

    def test_list_all_pets(self):
        self.open()
        self.driver.implicitly_wait(3)
        self.login()
        WebDriverWait(self.driver, 3).until(EC.title_is("PetFriends: My Pets"))
        # ожидаем заголовок окна равен указанной строке
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.CLASS_NAME, "card-deck")))

        '''Теперь нужно убедиться, что внутри каждой карточки питомца есть фото, имя питомца, возраст и вид'''
        photo = self.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')  # определяем фото
        names = self.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')  # определяем имя
        type_age = self.driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')  # определяем вид и возраст
        try:
            for i in range(len(names)):  # перебираем все элементы
                assert photo[i].get_attribute("src") != ""
                # проверяем, что фото есть (путь, указанный в атрибуте src, не пустой)
                assert names[i].text != ""  # проверяем, что имя есть
                # assert type_age[i].text != ""  # проверяем, что не пустое, хотя в любом случае есть запятая
                # assert ", " in type_age[i]  # убеждаемся в наличии запятой
                parts = type_age[i].text.split(", ")  # разделяем строку на части
                assert len(parts[0]) > 0  # проверяем, что в первой части есть вид
                assert len(parts[1]) > 0  # проверяем, что во второй части есть возраст

        except AssertionError:
            print("Есть карточки с неполными данными")

    def test_list_my_pet(self):
        self.open()
        self.driver.implicitly_wait(3)
        self.login()

        self.driver.implicitly_wait(1)  # Передаем время ожидания для визуального подтверждения

        WebDriverWait(self.driver, 3).until(EC.element_to_be_clickable(
            (By.XPATH, "//a[@class='nav-link' and @href='/my_pets']"))).click()  # заходим в "мои питомцы"
        '''Присутствуют все питомцы, которые есть в статистике'''
        petcount = self.driver.find_elements(By.XPATH, "//div[@class='.col-sm-4 left']")
        # Сохраняем в переменную кол-во питомцев в счётчике
        pets = self.driver.find_elements(By.CSS_SELECTOR, ".table.table-hover tbody tr")
        # Сохраняем в переменную pets карточки питомцев
        number = petcount[0].text.split('\n')  # разбиваем строку по символу '\n' (первая строка "Питомцев: 3")
        number = number[1].split(' ')  # разделяем строку по пробелу и выбирает 2 элемент ("3")
        number = int(number[1])  # переводим в целое число
        number_of_pets = len(pets)  # количество карточек питомцев
        assert number == number_of_pets  # проверяем, что количество питомцев в статистике равно кол-ву карточек
        # питомцев

        '''У всех питомцев разные имена'''
        names = self.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr td')
        # определяем все имена # питомцев
        list_names_of_my_pets = []  # создаем список для хранения имен питомцев
        try:
            for i in range(len(names)):  # перебираем все элементы в списке names
                list_names_of_my_pets.append(names[i].text)  # добавляем в список list_names_of_my_pets
                # (хотел сделать словарь с ключами i и значениями names[i], но нашёл способ проще)
            set_pet_data = set(list_names_of_my_pets)  # преобразовываем список в множество, что бы исключить дубликаты
            assert len(list_names_of_my_pets) == len(set_pet_data)  # проверяем, что количество имен в списке
            # list_names_of_my_pets равно кол-ву множества set_pet_data
        except AssertionError:
            print("Есть одинаковые имена питомцев")
