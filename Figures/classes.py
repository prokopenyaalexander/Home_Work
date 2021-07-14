import math

"""
Создаем класс Point
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
Создаем класс Figure
"""


class Figure:
    def __init__(self, pi=3.14):
        self.pi = pi

    def length_line(self, x, y, x1, y1):
        return math.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)


"""
Описываем Круг
"""


class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def circle_area(self):
        return self.pi * self.radius ** 2

    def circle_perimeter(self):
        return 2 * self.pi * self.radius


"""
Описываем Треугольник
"""


class Triangle(Figure):
    def __init__(self, x, y, x1, y1, x2, y2):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.a = super().length_line(self.x, self.y, self.x1, self.y1)
        self.b = super().length_line(self.x1, self.y1, self.x2, self.y1)
        self.c = super().length_line(self.x, self.y, self.x2, self.y2)

    def tr_per(self):
        return self.a + self.b + self.c

    def triangle_area(self):
        return math.sqrt(self.tr_per() * (self.tr_per() - self.a) * (self.tr_per() - self.b) * (self.tr_per() - self.c))


"""
Создаем класс квадрат
"""


class Square(Figure):
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.side = math.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)

    def square_area(self):
        return self.side ** 2

    def square_perimeter(self):
        return self.side * 4
