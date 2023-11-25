# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
# Программа должна подсказывать “больше” или “меньше” после каждой попытки.
# Для генерации случайного числа используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
from random import randint
user_count = 1
try_count = 10
N = randint(LOWER_LIMIT, UPPER_LIMIT)
print(N)
K = int(input("Угадайте целое число от 1 до 1000:"))
while K != N:
    if K < N:
        print("Ваше число меньше, чем задумал компьютер")
    elif K > N:
        print("Ваше число больше, чем задумал компьютер")
    K = int(input(f'Повторите попытку у вас осталось {try_count} попыток: '))
    try_count -= 1
    user_count += 1
    if user_count > 10:
        break
if K == N:
    print("вы выиграли")
else:
    print("вы проиграли")



