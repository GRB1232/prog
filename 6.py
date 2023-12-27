n = int(input('Введите целое число n '))
for i in range(n):
    a = n/3
    n = a
    if n == 1:
        print(True)
        break
if n != 1:
    print(False)
