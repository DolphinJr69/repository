# Необходимо ввести сумму, которую нужно накопить. Далее вводить значения, пока не накопится нужная сумма.
# Например:
# Сколько хотите накопить? 100
# Взнос: 10
# Взнос: 30
# Взнос: 70
# Поздравляю! Вы накопили 110 сомов!

a = map(int, input())
x = 1000
if a == x:
    print('ДА')
else:
    print('НЕТ')


