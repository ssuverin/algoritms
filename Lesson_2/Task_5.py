# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел
# выполняется равенство: 1 + 2 + ... + n = n(n + 1) / 2, где n — любое натуральное
# число.

def summa(n):
    if n == 1:
        return n
    return n + summa(n - 1)


last = int(input('Введите натуральное число - '))
first = summa(last)
second = int(last * (last + 1) / 2)
print(f'Левая часть уравнения - {first}')
print(f'Правая часть уравнения - {second}')

if first == second:
    print('Выражения равны')
else:
    print('Выражения не равны')
