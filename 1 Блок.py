def sum_of_positive_numbers(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum

user_input = int(input("Введите число: "))
result = sum_of_positive_numbers(user_input)
print("Сумма первых", user_input, "положительных чисел равна", result)
