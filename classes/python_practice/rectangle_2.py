from rectangle import Rectangle,Square,Circle
# Создаем два прямоугольника

rect_1 = Rectangle(3,4)
rect_2 = Rectangle(12,5)
# Выводим площадь наших двух прямоугольников
# print(rect_1.getArea())
# print(rect_2.getArea())

square_1 = Square(5)
square_2 = Square(10)

circle_1 = Circle(3)
circle_2 = Circle(10)
# print(square_1.get_area_square(),square_2.get_area_square())
figures = [rect_1,rect_2,square_1,square_2,circle_1,circle_2]
for figure in figures:
    if isinstance(figure,Rectangle):
        print(figure.getArea())
    elif isinstance(figure,Circle):
        print(round(figure.get_area_circle(),2))
    else:
        print(figure.get_area_square())