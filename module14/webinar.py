# Синтаксис функции
# def имя функции(аргументы)
#   инструкции
#   return список выражений

# def greet(name):
#     print("Привет"+ name + "Доброе утро")
# greet("john")
# Возвращаемое значение return
# def absolute_value(num):
#     if  num >=0:
#         return num
#     else:
#         return -num
# print(absolute_value(10))
# print(absolute_value(-5))
# область видимости(scope) и время жизни переменных
#
# def my_func():
#     x =2
#     print("значение внутри функции",x)
# x = 20
# my_func()
# print("Значение вне функции",x)
# Аргументы функции
# фиксированное количество аргументов
# def greet(name, age):
#     print(f"Привет    { name }    Доброе утро    мне   {age}  год")
# greet("john" ,51)
# аргументы по умолчанию
# def greet(name="Имя", age=0):
#     print(f"Привет    { name }    Доброе утро    мне   {age}  год")
# greet("Петя",45)
# Именованый аргумент
# def greet(name="Кто?", age=0):
#     print(f"Привет    {name}    Доброе утро    мне   {age}  год")
#
#
# greet("john", 51)
# greet(name="Вася", age=48)
# произвольный список аргументов
# *
# def greet(*names):
#     for name in names:
#         print("Привет   ", name)
# greet("Света","Клава","Вася","Дядя Игорь")
# Кортеж(ф,ы,в)
# Список [a,s,d]
# Словарь{q:2,w:3,e:4}
# a={'q':2,'w':3,'external':5}
# print(a.values())
# print(a.keys())
# def adder(*nums):
#     sum= 0
#     for i in nums:
#         sum += i
#
#     print('sum' ,sum)
# adder(1,2,3,4,5,6,7)
# x= "global variable"
# def foo():
#     global x
#     y = "local variable"
#     x = x*2
#     print(x)
#     print(y)
# foo()
# нелокальные переменные nonlocal
# def outer():
#     x = " локальная переменная"
#     def inner():
#         nonlocal x
#         x = "нелокальная переменная"
#         print("вложенная функция", x)
#     inner()
#     print(":", x)
# outer()
def say():
    greeting = "привет"
    def display():
        print(greeting)
    display()
say()
