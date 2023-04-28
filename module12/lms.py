# # Вариант 1
# number = '1 2 3 4 5 6 7'
# str_number = number.split()
# print('\n'.join(str_number))
# # Вариант 2
# number = '1 2 3 4 5 6 7'
# number_str = '\n'.join(number.split())
# print(number_str)
# age = 25
#
# my_age = "I'm %d years old" % (age) # в шаблоне присутствует специальный символ %d
#
# print(my_age)
# s = [0, 'hello',(1,'a')]
# print(s)
# объект.метод
# a, b, c, d = 'эй', "би ", "си","ди"
# letters = []
# letters.append(a)
# letters.append(b)
# letters.append(c)
# letters.append(d)
# print(letters)
# print(letters[len(letters)-1])
# letters.pop()
# print(letters)
# letters.append('упс')
# print(letters)
# letters.pop(0)
# print(letters)
# letters.append('врагу ,не сдается')
# print(letters)
# letters.pop(3)
# letters.append("наш городый Варяг")
# print(letters)
# L = ["а", "б", "в", 1, 2, 3, 4]
# print (L[-1:-4:-1])
# string = input("Введи числа через пробел:")
# list_of_string = string.split()# список строковых представлений данных
# list_of_string = list(map(int,list_of_string))# список чисел
# print(sum(list_of_string[::3]))

# все операции - деление строки по пробелам, преобразование к числам
# и приведение объекта map к типу список, можно делать в одной строке
# L = list(map(float, input("Введите числа через пробел").split()))
#
# # обмениваем первое и последнее число
# # с помощью множественного присваивания
# L[0], L[-1] = L[-1], L[0]
#
# # находим сумму и добавляем её в конец списка
# L.append(sum(L))
#
# print(L)
# name = input("Введите ваше имя")
# name_start = name[1:].lower()
# name_end = name[0].upper()
# res = name_end + name_start
# print(res)

# person = {} # с помощью фигурных скобок можно создать словарь
#
# # словарь заполняется по принципу - ключ:объект (через двоеточие)
# person = {'name' : 'Ivan Petrov'}
#
# # в него можно также добавлять новые объекты по ключу
# person['age'] = 25
# person['email'] = 'ivan_petrov@example.com'
# person['phone'] = '8(800)555-35-35'

# print(person)
# # {'name': 'Ivan Petrov', 'age': 25, 'email': 'ivan_petrov@example.com', 'phone': '8(800)555-35-35'}
# person = {}
# person["name"] = "Руслан"
# person["возраст"]= 52
# person["самочувствие"] = "ебливое"
# print(person)
# print(person.keys())
# print(person.values())
# person.pop("самочувствие")
# print(person)
# d = {'day' : 22, 'month' : 6, 'year' : 2015}
#
# print("||".join(d.keys()))
# title = "Бронекорабли"
# author = "Иванов"
# year = "2022"
# book ={'title': title, 'author':author, 'year': int(year)}
#
# print(book)
# abit1 = {"ФИО" : 'Фадеев О.Е.', "Количество баллов" : 283, "Заявление" : True}
# abit2 = {"ФИО" : 'Дружинин И.Я.', "Количество баллов" : 278, "Заявление" : False}
# abit3 = {"ФИО" : 'Афанасьев Д.Н.', "Количество баллов" : 276, "Заявление" : True}
#
#
# abits = [abit1, abit2, abit3]
#
# print(abits)
# abit4 = {"ФИО" : 'Любимчиков А.Я.', "Количество баллов" : 269, "Заявление" : True}
#
# abits.append(abit4)
#
# print(abits)
# L = ['a', 'b', 'c']
# print(id(L))
#
# L.append('d')
# print(id(L))
# a = 5
# b = 3+2
# rasn = id(a)-id(b)
# print(rasn)
shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print( list_id_before is list_id_after )
