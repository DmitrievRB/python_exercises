# def char_frequence():
#     text = str(input("Введите текст"))
#     text = text.lower()
#     text = text.replace(" ", "")
#     text = text.replace("\n", "")
#     count = {}  # для подсчета символов и их количества
#     for char in text:
#         if char in count:  # если символ уже встречался, то увеличиваем его количество на 1
#             count[char] += 1
#         else:
#             count[char] = 1
#     for char, cnt in count.items():
#         print(text)
#         print(count)
#         print(f"Символ {char} встречается {cnt} раз")
#
# char_frequence()
# def addition_a_and_b():
#     a = 2
#     b = 2
#     print(a+b)
# addition_a_and_b()
# def reverse_stair(n):
#    for i in range(n, 0, -1):
#        print("*" * i)
#
# reverse_stair(5)
# def count_divider(a):
#     count = 0
#     for n in range (1,a+1):
#         if a % n == 0:
#             count += 1
#     print(count)
#     return count
# count_divider(10)
# def try_polindrom( text = "Кит на море не романтик"):
#     text = text.lower()
#     text = text.replace(" ","")
#     # revers_text = "".join(reversed(text))
#     revers_text = text[::-1]
#
#     if  text ==revers_text:
#         return True
#     else:
#         return False
# print(try_polindrom())
# try_polindrom("Лёша на полке клопа нашёл")

# PI = 3.14 #Глобальная переменная
# def area_circle(r=int(input("Введи обхват"))):
#     return r/PI
# print(area_circle())
# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# # [[1, 2, 3], 4, 5, 6]
#
# a = [1, 2, 3]
# b = [*a, 4, 5, 6]
# print(b)
# # [1, 2, 3, 4, 5, 6]
# print(a) # [1, 2, 3]
# print(*a)  # 1 2 3
# def adder(*nums):
#     sum_ = 1
#     for n in nums:
#         sum_ *= n
#
#     return sum_
#
#
# print(adder())  # 0
# print(adder(1))  # 1
# print(adder(1, 2))  # 3
# print(adder(2, 2, 2,2,2,2,2,2,2))  # 6
# def incorrect_func(name_arg=[]):
#    # name_arg является локальной переменной
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# incorrect_func()
# print('-----')
# incorrect_func()
# incorrect_func()
# incorrect_func()
# print('-----')
# def correct_func(name_arg=None):
#    if name_arg is None:
#        name_arg = []
#    print("Аргумент до изменения", name_arg)
#    name_arg.append(1)
#    print("Аргумент после изменения", name_arg)
#
# # вызовем два раза одну и ту же функцию
# correct_func()
# print('-----')
# correct_func()
# correct_func()
# def factorial_recursive(n):
#     if n ==1:
#         return n
#     else:
#         return n*factorial_recursive(n-1)
# num =3
# print(f"factorial  {num} это {factorial_recursive(num)} ")
# def summ_number(n):
#     if n==1:
#         return n
#     else:
#         return n+summ_number(n-1)
# num=10
# print(f"Сумма {num} чисел  {summ_number(num)}")
def fib():
    a,b = 0,1
    yield a #F0
    yield b # F1
    while b <9999:
        a, b = b, a +b
        yield b
for num in fib():
    print(num)






