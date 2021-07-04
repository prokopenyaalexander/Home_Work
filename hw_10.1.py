"""
Создать пять классов описывающие реальные объекты. Каждый класс
должен содержать минимум три приватных атрибута, конструктор, геттеры
и сеттеры для каждого атрибута, два метода.
"""
class Laptop():
    def __init__(self,manufacturer, price, color, weight, country, sound, screen):
        self.manufacturer = manufacturer
        self.price = price
        self.color= color
        self.weight = weight
        self.__country = country
        self.__sound = sound
        self.__screen = screen

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, country):
        self.__country = country  


class Country():
    def __init__(self,population, square, avg_salary, nation, sea, ocean ):
        self.population = population
        self.square = square
        self.avg_salary= avg_salary
        self.__nation = nation
        self.__sea = sea
        self.__ocean = ocean


    @property
    def nation(self):
        return self.__sea

    @nation.setter
    def nation(self, nation):
        self.__nation = nation


class fruit():
    def __init__(self,manufacturer, price, size, weight, color, country, production):
        self.manufacturer = manufacturer
        self.price = price
        self.size = size
        self.weight = weight
        self.__color = color
        self.__country = country
        self.__production = production
    

    @property
    def color(self):
        return self.__color


    @color.setter
    def color(self, color):
        self.__color = color


class Human():
    def __init__(self,nation, height, weight, work, date_of_birthday, gender):
        self.nation = nation
        self.height = height
        self.weight = weight
        self.__work = work
        self.__date_of_birthday = date_of_birthday
        self.__gender = gender

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        self.__gender = gender


class Flat():
    def __init__(self,square, price, rooms, floor, doors, beds):
        self.square = square
        self.price = price
        self.rooms = rooms
        self.__floor = floor
        self.__doors = doors
        self.__beds = beds

    
    @property
    def floor(self):
        return self.__floor


    @floor.setter
    def floor(self, floor):
        self.__floor = floor

my_flat = Flat(5,2,5,6,5,4)
my_flat.floor = 17
print(my_flat._Flat__floor)

