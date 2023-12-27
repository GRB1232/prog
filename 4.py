a = int(input('Введите целое число А (A<B)'))
b = int(input("Введите целое число B "))
all = 0
even = 0
odd = 0
for i in range(a,b+1):
    all += i
    if i%2 == 0:
        even += i
    else:
        odd += i
print('Общаая сумма =',all,"Сумма четных чисел =",even,"Сумма нечетных чисел =",odd)