x = float(input("Введите расстояние поездки в км    "))
def taxi(x):
    if x >= 0.14:
        x = x * 1000 / 140 * 15 + 240
    else:
        x = 240
    return x


print('стоимость поездки составит', int(taxi(x)),'руб.')

