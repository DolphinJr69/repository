# Напишите программу, которая определяет,
# является число четным или нечетным.
# На вход программе подаётся одно целое число.
# Программа должна вывести «Четное»,если число четное,
# и «Нечетное» — если число нечетное.


a = int(input('Введите число - '))
if a % 2 == 0:
    print('Четное')
else:
    print('Нечетное')
