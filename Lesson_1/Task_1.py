# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
x = int(input('Введите трехзначное число: '))
x1 = x // 100
x2 = x % 100 // 10
x3 = x % 10
print(f'Сумма цифр числа равна - {x1 + x2 + x3}')
print(f'Произведение цифр числа равна - {x1 * x2 * x3}')