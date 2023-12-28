A = int(input("Введите положительное число A: "))
B = int(input("Введите положительное число B: "))
C = int(input("Введите положительное число C: "))

f = 0
while A >= C:
    A -= C
    B1 = B
    while B1>= C:
        B1 -= C
        f += 1
print (f)
