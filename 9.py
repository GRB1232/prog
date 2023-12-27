num = int(input("введите число: "))
def nums (num):
    if 1<=num<=12:
        numerals = ['первое', "второе", "третье", "четвертое", "пятое", "шестое", "седьмое", "восьмое", "девятое", "десятое", "одиннадцатое", "двеннадцатое"]
        a = numerals[num-1]

    else:
        a = ('')
    return a
if __name__ == "__main__":
    print(nums(num))
    print('числа по порядку: ')
    for i in range(1,13):
        print(nums(i))







