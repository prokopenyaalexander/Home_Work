from func import *


def main():
    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Создание: add\n"
              "Чтение: read\n"
              "Обновление по ID: update\n"
              "Удаление по ID: delete\n"
              "Выход: q\n")
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        if action == 'add':
            name = (input("name = "))
            price = float(input("price = "))
            quantity = int(input("quantity = "))
            comments = input("comment = ")
            add(name, price, quantity, comments)
        if action == 'update':
            print("Введите номер ID")
            numb = int(input())
            name = (input("name = "))
            price = float(input("price = "))
            quantity = int(input("quantity = "))
            comments = input("comment = ")
            update(name, price, quantity, comments, numb)
        if action == 'delete':
            print("Введите номер ID")
            numb = int(input())
            delete(numb)
        if action == 'read':
            read()


if __name__ == '__main__':
    main()
