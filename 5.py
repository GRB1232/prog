a = float(input('Введите длинну отрезка А (A>B) '))
b = float(input('Введите длинну отрезка В '))
st = a
while st >= b:
    st -= b
print("Длина не занятой части отрезка А равна",round(st, 2))