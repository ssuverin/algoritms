# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано,
# вывести правильный ответ.

import random

rand_number = random.randint(0, 100)
attempt = 0

while attempt <= 10:
    user_number = int(input('Введите число: '))
    attempt += 1
    if user_number == rand_number:
        print(f'Вы угадали число {rand_number} с {attempt} попытки')
        break
    elif user_number > rand_number:
        print(f'Не угадали. Меньше')
    else:
        print(f'Не угадали. Больше')
if attempt == 0:
    print(f'Вы не угадали число {rand_number}')
