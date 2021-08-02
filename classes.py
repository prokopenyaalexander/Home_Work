import math
"""
Class Point
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


"""
class Figure
"""


class Figure:
    def __init__(self,  pi=3.14):
        self.pi = pi

    def length_line(self, x: Point, y: Point, x1: Point, y1: Point):
        return math.sqrt((x1 - x) ** 2 + (y1 - y) ** 2)


"""
class Circle
"""


class Circle(Figure):
    def __init__(self, x: Point, y: Point, radius):
        super().__init__()
        self.x = x
        self.y = y
        self.radius = radius

    def circle_area(self):
        return self.pi * self.radius ** 2

    def perimetr_circle(self):
        return 2 * self.pi * self.radius


"""
class Triangle
"""


class Triangle(Figure):
    def __init__(self, x: Point, y: Point, x1: Point, y1: Point, x2: Point, y2: Point):
        super().__init__()
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.a = super().length_line(self.x, self.y, self.x1, self.y1)
        self.b = super().length_line(self.x1, self.y1, self.x2, self.y2)
        self.c = super().length_line(self.x, self.y, self.x2, self.y2)

    def tr_per(self):
        return self.a + self.b + self.c

    def triangle_area(self):
        return math.sqrt(self.tr_per() * (self.tr_per() - self.a) * (self.tr_per() - self.b) * (self.tr_per() - self.c))


"""
class Square
"""


class Square(Figure):
    def __init__(self, x, y, x1, y1):
        super().__init__()
        self.x = x
        self.y = y
        self.x1 = x1
        self.y1 = y1
        self.side = math.sqrt((self.x1 - self.x) ** 2 + (self.y1 - self.y) ** 2)

    def square_area(self):
        return self.side ** 2

    def square_perimeter(self):
        return self.side * 4
