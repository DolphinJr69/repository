# a = input('Введите свое имя - ').lower()
# total = 0
# for i in a:
#     if i == 'a':
#         total += 1
# print(total, 'a')

#
# a = ['123', 234, 'abrakadabra', 56754]
# x = []
# for i in a:
#     if type(i) == type(''):
#         x.append(i)
# print(x)

numbers = [2, 4, 7, 1, 8.4, -3.3, 7.1, -2, 4, -1, 7, -43, 8, -3, 6, 9]
total = 0
for i in numbers:
    if int(i) % 2 == 0:
        numbers.append(i)
print(numbers)