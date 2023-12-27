import sys

a = float(input('Введите число А '))
b = float(input('Введите число В '))
c = float(input('Введите число С '))
if a<=0 or b<=0 or c<=0:
    print('Ошибка. Число должно быть больше нуля.')
    sys.exit()

ab = a * b
sqC = c ** 2
summ = ab
done = 0
while summ>= sqC:
    summ -= sqC
    done += 1
print('В прямоугольник AB поместятся',done,'квадратa(ов) со стороной С')

