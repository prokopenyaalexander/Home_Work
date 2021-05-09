# 1. Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.

# 2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.

# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.
"""Дополнительные задачи"""
# 4. Нужно посмотреть, в какое время дня у баристы были перерывы в работе.
# Для этого, нужно взять все покупки за каждый день, сравнить время между ними и отобразить промежутки больше часа.

# 5. После перерасчёта оказалось, что для окупаемости, каждый день в кафе должно продаваться не меньше 20 чашек кофе.
# Надо написать декоратор, который будет проверять кол-во чашек кофе на каждый день. И если их было меньше 20,
# возвращать сообщение с ошибкой (подсказка: try/except).

################################################################################
# 1. Каждый день в кафе заходит от 5 до 20 покупателей. Каждый покупатель берёт от 1 до 3 чашек кофе.
# Нужно написать функцию, которая будет генерировать тестовые данные при каждом вызове.
import random
import datetime
from random import randrange
from datetime import timedelta

def order():
    coffee_dict = {}
    customers = random.randrange(5, 7)

    for customer in range(customers):
        customer += 1
        coffee_mug = random.randrange(1, 4)
        coffee_dict[customer] = coffee_mug
    # print(coffee_dict)
    return coffee_dict

# 2. К каждой покупке нужно добавить дату и время до минуты (2 отдельные переменные).
# Время работы кафе - с 9 до 20 часов.


def time_func():
    coffee_dict = order()
    time_list = []

    for customer in coffee_dict:

        d1 = datetime.date(2021, 4, 28)     # start date
        d2 = datetime.date(2021, 5, 2)      # end date

        delta = d2 - d1                     # timedelta
        date_list = []
        if delta.days <= 0:
            print("ERROR")
        for i in range(delta.days + 1):
            hours = random.randrange(9, 20)
            minutes = random.randrange(0, 60)
            r_date = d1 + timedelta(i)
            date_list.append(str(r_date))
        time_list.append((hours, minutes))
        time_list.sort()

    #print(date_list)
    #print(time_list)
    res = {}
    for date, time in zip(date_list, time_list):
        res[date] = time
    #print(res)
    return res
time_func()

# 3. Кафе работает 5 дней в неделю. В конце недели надо составить отчёт по кол-ву клиентов и покупок.

def report():
    coffee_dict = order()
    time_list = time_func()
    sum_customers = 0
    sum_coffee_mug =0
    for days in range(1, 6):
        coffee_dict = order()
        print("Кол-во поситетелей в",days,"-й день", sum(coffee_dict.keys()), "Чашек кофе:", sum(coffee_dict.values()))
        sum_customers += sum(coffee_dict.keys())
        sum_coffee_mug += sum(coffee_dict.values())
    print("Количество покупателей за неделю", sum_customers, "Чашек кофе", sum_coffee_mug)


report()



