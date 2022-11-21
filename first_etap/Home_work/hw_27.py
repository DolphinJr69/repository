# Напишите проверку на то, является ли строка палиндромом.
# Палиндром — это слово или фраза, которые одинаково читаются слева направо и справа налево.
# Пример:
# # # тот -> тот
# # # потоп -> потоп
# # # көк -> көк
# СЛОВА ДЛЯ ПРОВЕРКИ:
# words = ['Anna', 'Civic', 'Kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопку',]
students = {'Sonun', 'Danila', 'Roman', "Erkin", 'Abdymazhit', 'Natalia', 'Saltanat', 'Ali', 'Nuriza'}
com1 = []
com2 = []
com3 = []
print(students)
for i in range(3):
	com1.append(students.pop())

for i in range(3):
	com2.append(students.pop())

for i in range(3):
	com3.append(students.pop())



print(com1)
print(com2)
print(com3)