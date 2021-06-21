def fact(n):
    while n < 0:
        print("Неверный ввод, введите n > 0")
        n = int(input())

    res = 1
    if n % 2 == 0:
        for i in range(1,n,2):
            i += 1
            res *= i
    else:
        for i in range(1,n + 1, 2):
            res *= i
    print(res)

fact(int(input("Введите N ")))

    