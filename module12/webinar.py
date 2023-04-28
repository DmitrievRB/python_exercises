# Task_1
# Запрашиваем ввод слов от пользователя пока не введет пустую строку
# words = input("Введи слово")
# book = []
# while words != "":
#     # добавляем в массив только если не повторяются слова
#     if words not in book:
#         book.append(words)
#     words = input()

# for letters in book:
#     # letters.sort(reverse=True)
#     print(letters, end=" ")
#     print(len(letters), end=" ")
#
#Task_2
    # Запрашиваем вdод чистла от пользователя пока он не введет 0
num = int(input())
# Значения помещаются в список (массив)
data = []
while num != 0:
    data.append(num)
    num = int(input())
    # выводим список отсортированым
data.sort()
print(data,end='')
# # Task_3
# # запрашиваем входящую букву
# letter = input('input letter')
# # если буква принадлежит к выбраным
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     # Вывести гласная
#     print('гласная буква')
#     # если к выбраным то
# elif letter == 'y':
#     # вывести такая и такая
#     print('согласная и гласная буква')
#     # Иначе
# else:
#     # Вывести согласная
#     print('согласная буква')
#     # Task_4
#     # Запрашиваем вdод чистла от пользователя пока он не введет 0
# num = int(input())
# # Значения помещаются в список (массив)
# data = []
# while num != 0:
#     data.append(num)
#     num = int(input())
#     # выводим список отсортированым
# data.sort()
# print(data,end='')
#
