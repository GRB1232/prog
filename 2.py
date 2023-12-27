a = int(input("Введите целое число a: "))
b = int(input("Введите целое число b (b>a): "))
if b <= a:
    print("Ошибка. b>a")
else:
    print("Целые числа между a и b:")
    count = 0
    for i in range(a, b + 1):
        print(i)
        count += 1

    print("Количество чисел:", count)
