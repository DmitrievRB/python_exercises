# a = [1, 2, 3]
# print(id(a))  # id возвращает идентификатор объекта
# # 140039772293512
# b = a
# print(id(b))
# a.append(4)
# # 140039772293512
# print(a is b)  # а и b являются один и тем же объектом
# # True
# is_rainy = False  # дождь будет
#
# if is_rainy:
#     print("Брать зонт")
# else:
#     print("Не брать зонт"
# mx = 0
# s = 0
# x = int(input())
# if x < 0:
#     s = x
# b = 7
# b /= b
# if x > mx:
#     mx = x
# print(s)
# print(mx)
# is_rainy = True  # дождь будет
# heavy_rain = False  # не сильный дождь
#
# if is_rainy:
#     # в данный блок дописали ещё один условный оператор
#     if heavy_rain:
#         print("Брать зонт")
#     else:
#         print("Надеть дождевик")
# else:
#     print("Не брать зонт")
# try:  # Добавляем конструкцию try-except для отлова нашей ошибки
#     print("Перед исключением")
#     # теперь пользователь сам вводит числа для деления
#     a = int(input("a: "))
#     b = int(input("b: "))
#     c = a / b  # здесь может возникнуть исключение деления на ноль
#     print(c)  # печатаем c = a / b если всё хорошо
# except ZeroDivisionError as e:  # Добавляем тип именно той ошибки которую хотим отловить.
#     print(e)  # Выводим информацию об ошибке
#     print("После исключения")
#
# print("После После исключения")
#
# try:
#     a = int(input("Введите число:\t"))
#     print(f"Вы ввели{a}")
# except ValueError:
#     print("Вы ввели не правильное число")
# else:
#     print("Спокойно выходим из программы")
# finally:
#     print("Вот и все")

# def get_wind_class(speed):  # Объявление функции
#     if 1 <= speed <= 4:
#         return "weak [1]"
#     elif 5 <= speed <= 10:
#         return "moderate [2]"
#     elif 11 <= speed <= 18:
#         return "strong [3]"
#     elif speed >= 19:
#         return "hurricane [4]"
# get_wind_class(2)

# user_database = {'user': 'password', 'iseedeadpeople': 'greedisgood','hesoyam': 'tgm'}

# def check_user(username, password):
#     if username in user_database:
#         if password == user_database[username]:
#             return True
#         else:
#             return False
#     else:
#         return False
# check_user('hesoyam','tgm')
L = [int(input()) % 2 == 0 for i in range(5)]
print( any(L))

