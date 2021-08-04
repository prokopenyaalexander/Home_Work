from func import *
from exceptions import *


def main():
    while True:
        print("Выберите действие которое хотите сделать:\n"
              "Сложение: +\n"
              "Вычетание: -\n"
              "Умножение: *\n"
              "Деление: /\n"
              "Выход: q\n")
        action = input("Действие: ")
        if action == "q":
            print("Выход из программы")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                summary(x, y)
            if action == '-':
                difference(x, y)
            if action == '*':
                multiple(x, y)
            if action == '/':
                zero_exception(x, y)
                division(x, y)


if __name__ == '__main__':
    main()
