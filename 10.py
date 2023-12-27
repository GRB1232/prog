import math

a = float(input('Введите длину катета А '))
b = float(input('Введите длину катета B '))
def pifagor(a,b):
    return round(math.sqrt(a**2+b**2),2)
print(pifagor(a,b))
