from func import *


def main():
    print("Выберите таблицу")
    tbl = input("Таблица: ")
    if tbl == 'Car':
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
                model = (input("model = "))
                release_year = float(input("release_year = "))
                brand = (input("brand = "))
                add(model, release_year, brand)

            if action == 'update':
                print("Введите номер ID")
                numb = int(input())
                model = (input("model = "))
                release_year = float(input("release_year = "))
                brand = int(input("brand = "))
                update(model, release_year, brand, numb)

            if action == 'delete':
                print("Введите номер ID")
                numb = int(input())
                delete(numb)

            if action == 'read':
                read()
    elif tbl == 'Brand':
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
                add_two(name)

            if action == 'update':
                print("Введите номер ID")
                numb = int(input())
                name = (input("name = "))
                update_two(name, numb)

            if action == 'delete':
                print("Введите номер ID")
                numb = int(input())
                delete_two(numb)

            if action == 'read':
                read_two()


if __name__ == '__main__':
    main()
