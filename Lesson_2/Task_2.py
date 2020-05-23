# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560,
# в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5)

number = int(input('Введите натуральное число - '))
num_odd = 0
num_non_odd = 0

while number > 0:
    if number % 2 == 0:
        num_odd += 1
    else:
        num_non_odd += 1
    number = number // 10
print(f'В числе {number} {num_odd} четных цифры и {num_non_odd} нечетных.')