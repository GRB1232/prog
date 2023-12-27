price = float(input('Введите цену за один киллограм '))
mult = 1
vl = 1
for i in range(11):
    if mult <= 2:
        print("Цена за", round(vl,2),"кг.", round(price * mult,2), "руб.")
        vl += 0.2
        mult += 0.2

