"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость(по
умолчанию 0). Методы: увеличить скорости(скорость + 5), уменьшение
скорости(скорость - 5), стоп(сброс скорости на 0), отображение скорости,
разворот(изменение знака скорости). Все атрибуты приватные.
"""

class Car():
    #конструктор
    def __init__(self, brand : str, model : str, year_of_creation : int, speed=0):
        self.__brand = brand
        self.__model = model
        self.__year_of_creation = year_of_creation
        self.__speed = speed

    
    def increase_speed(self, speed_up=5):
        self.__speed += speed_up
        return self.__speed

    
    def decrease_speed(self, speed_down=5):
        self.__speed = 7
        self.__speed -= speed_down
        return self.__speed

    
    def stop_speed (self):
        self.__speed = 0
        return self.__speed


    def u_turn(self):
        self.__speed = 5
        return -(self.__speed)

car_1 = Car("Lada", "Vesta", 2021, 0)
print(car_1._Car__brand, car_1._Car__model, car_1._Car__year_of_creation, car_1._Car__speed)
print(car_1.increase_speed())
print(car_1.decrease_speed())
print(car_1.stop_speed())
print(car_1.u_turn())

