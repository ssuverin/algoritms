# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

number = int(input('Введите число - '))
tmp_number = 0
last = 0

while number > 0:
    last = number % 10
    number = number // 10
    tmp_number *= 10
    tmp_number += last
print(f'Обратное чило - {tmp_number}')