# # # #Создали массив , список
# # # mas = [23,'helo',True]
# # # #Выводим к консоль первый и последний элемент массива
# # # print(mas[0])
# # # print(mas[-1])
# # #
# # # # #Выводим список в консоль с диапозоном от 1 до 100 с шагом 5 если занчения четные
# # # # for i in range(100,0,-5):
# # # #     if i % 2 ==0:
# # # #         print(i,end=' ')
# # #
# # # # name=[2,4,7,1,5,9,]
# # # # for x in name:
# # # #     if x >4:
# # # #         print(x,end=' ')
# # # # edibles=["отбивные","пельмени","яйца","орехи"]
# # # # for food in edibles:
# # # #     if food =="пельмени":
# # # #         print("Я не ем пельмени!")
# # # #         break
# # # #     print("Отлично,вкусные" +" "+ food)
# # # # else:
# # # #     print("Хорошо,что не было пельменей!")
# # # # print("Ужин окончен.")
# # #
# # # a=3
# # # b=0
# # # while(a<6):
# # #     a+=4
# # #     b+=a
# # # print(b)
# # # Обмен значений переменных
# # a, b = -13, 7
# # a = a - b
# # b = b + a
# # a = b - a
# # print(a,b)
#
#
# date = (1, 'january', 2020)
# print(date)
# print(type(date))
# print(date[0])
# print(date[1])
# print(date[2])
# Webinar "типы данных"
# name = 'Ivan'
# Name = 'ivan'
#
# # camel case
# userName ='Tom'
# user_name ='Kate'
# Data Types
# типизация: динамическая и статическая
# Number
# a = 5 / 2
# b = 4 // 3
# c = 20 % 3
# d = 8 == 3
# e = round(10 / 3.0, 2)
# f = 10 / 3
# print(a, 'a')
# print(b, 'b')
# print(c, 'c')
# print(d, 'd')
# print(e, 'e')
# функция  преобразования - int () целочисленное преобразование
# b = int (f)
# print(f,b)
# float - вещественное ,дробное преобразование
# bin()
# print(bin(8))
# import math
#
# print(math.pow(2, 9))

# print(round(3.14159**2/2))
# s = 'Hello'
# print(s[0])
# # срез со второй по 4 буквы в слове
# print(s[3: :-1])
# print(s[-1])
# print(s.isalpha())
# Разбивка строки по цвету
# colors = 'red blue green'
# str_colors ='\n'.join(colors.split())
# print(str_colors)
# colors = 'red green blue'
# colors_split = colors.split() # список цветов по отдельности
#
# colors_joined = ' and '.join(colors_split) # объединение строк
# print(colors_joined)
# pi = 31.4159265
# print ("%.4e" % (pi))
# day = 14
# month = 2
# year = 2012

# print("%d.%02d.%d" % (day, month, year))
# # 14.02.2012
# print("%d-%02d-%d" % (year, month, day))
# # 2012-02-14
# print("%d/%d/%d" % (year, day, month))
# L = ["раз","раз","два","три"]
# b = set(L)
# print(b)
# b_list = list(b)
# print(b_list)

# text = input("Введите текст:")
#
# unique = list(set(text))
#
# print("Количество уникальных символов: ", len(unique))
# abons = {"Иванов", "Петров", "Васильев", "Антонов"}
#
# debtors = {"Петров", "Антонов"}
#
# non_debtors = abons.intersection(debtors)
#
# print(non_debtors)
# a = input("Введите первую строку: ")
# b = input("Введите вторую строку: ")
#
# a_set, b_set = set(a), set(b) # используем множественное присваивание
#
# a_and_b = a_set.symmetric_difference(b_set)
#
# print(a_and_b)