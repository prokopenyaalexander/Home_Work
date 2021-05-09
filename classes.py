# В отеле есть 3 типа номеров: royal (2-3 комнаты), lux (1-2 комнаты), standard (1 комната).
# надо добавить метод для создания номеров и хранения их в виде словаря
class Hotel:
    def __init__(self, room, quantity_of_room):
        self.room = room
        self. quantity_of_room = quantity_of_room

    def hotel_room(self, room, quantity_of_room):
        hotel_rooms = {}
        hotel_rooms[room] = quantity_of_room
        print(hotel_rooms)
        return hotel_rooms


hotel = Hotel('royal', 2)
hotel.hotel_room('royal', 2)


# В комнате есть мебель для ванной, спальни и зала (если есть зал).
# нужно добавить метод для добавления и удаления из комнаты мебели в любом количестве.
class Room:
    def __init__(self, furniture_for_bathroom, furniture_for_bedroom, furniture_for_hall):
        self.furniture_for_bathroom = furniture_for_bathroom
        self.furniture_for_bedroom = furniture_for_bedroom
        self.furniture_for_hall = furniture_for_hall

    def changes_in_room(self, furniture_for_bathroom, furniture_for_bedroom, furniture_for_hall):
        print("How many furniture for bathroom do you need?")
        print("Enter the quantity")
        answer = input()
        if answer == "no":
            print("Next step")
        else:
            self.furniture_for_bathroom = answer

        print("How many furniture for bedroom do you need?")
        print("Enter the quantity")
        answer = input()
        if answer == "no":
            print("Next step")
        else:
            self.furniture_for_bedroom = answer


        print("How many furniture for hall do you need?")
        print("Enter the quantity")
        answer = input()
        if answer == "no":
            print("Your order:")
        else:
            self.furniture_for_hall = answer
        print("Furniture for bathroom", self.furniture_for_bathroom)
        print("Furniture for bedroom", self.furniture_for_bedroom)
        print("Furniture for hall", self.furniture_for_hall)


order = Room(1, 1, 1)
order.changes_in_room(3, 5, 5)
