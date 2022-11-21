for i in range(10):
    print(i)

#
name = 'Python'
for i in name:
    print(i)

#
name = 'Python'
total = 0
for i in name:
    print(i)
    total += 1
print(f'В слове {name} {total} букв')

#
password = input('Введите пароль - ')
password2 = input('Повторите пароль - ')
total = 0
while password != password2:
    print('Пароли не схожи')
    total += 1
    password2 = input('Повторите пароли - ')
print('Вы вошли в аккаунт - ')
print('Всего попыток было', total)

#////////////////////////////////////////////////////////
#////////////////////////////////////////////////////////

users = ('dastan', 'saltanat', 'roman', 'erkinbek')
print(users[2][2])

#

users = ('dastan', 'saltanat', 'roman', 'erkinbek')
print(users[2][::-1])

#

users = ('dastan', 'saltanat', 'roman', 'erkinbek')
print(users[::-1])

#
names = ['Nuriz', 'Danila', 'Sonun']
for i in names:
    print(f'Имя - {i}')

#
names = ['Nuriz', 'Danila', 'Sonun']
for i in range(len(names)):
    print(f'{i} - {names}')

#
# names = ['Nuriz', 'Danila', 'Sonun']
# names.append(input('введите имя - '))
# print(names)
#
# #
# names = ['Nuriz', 'Danila', 'Sonun']
# for i in range(3):
# names.append(input('введите имя - '))
# print(names)

# #Недоделано
# names = ['Nuriz', 'Danila', 'Sonun']
# new_names = []
# for i in range(3):
#     new_names.append(input('введите имя - '))
# print(names)
# print(new_names)
# print(names.extend(names))

#
names = ['Nuriz', 'Danila', 'Sonun', 'Danila']
print(names.remove('Danila'))
print(names)

#
names = ['Nuriz', 'Danila', 'Sonun', 'Danila']
for i in range(names.count('Danula')):
    names.remove('Danila')
    print(names)

#
names = ['Nuriz', 'Danila', 'Sonun', 'Danila']
a = names.index('Sonun')

print(a)
print(names[a])

#
names = ['']
print(names[2:5])

#problem 1
kort = ['Roman', 22, 22.5, 185, 'R' ]
print(kort)

#problem 2
kort = ('Roman', 'Roma', 'Romanov')
print(kort[0], kort[1], kort[2])

#
a = [i for i in range(10)]
print(a)

#problem?
NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
for i in range(len(NAMES)//2):
    if i % 2 == 0:
        NAMES.pop(i)
print(NAMES)

#
das = [['312', (3, ['DAstan'])], [1, 2, 3, 4, ('dasd', 123, [132, 4])]]
print(das[0][1][1][0][1])

#
das = [['312', (3, ['DAstan'])], [1, 2, 3, 4, ('dasd', 123, [132, 4])]]
print(das[1][4][2][1])

#Создать пустой лист.
# Добавить в него сначала Ваше Имя, Год Рождения, любимый Язык Программирования.

a = []
name = input()
age = input()
prog = input()
a.append(name)
a.append(age)
a.append(prog)
print(a)

#Взять Лист №1 и посчитать сколько раз там встречается имя "Jack".

NAMES = ['JACK', 'JIMMY', 'JACKSON', 'JHON', 'JACKSON', 'JHON',  'JIMMY', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON', 'JACKSON', 'JHON','JACK', 'JIMMY', 'JACK', 'JACKSON', 'JHON',]
print(NAMES.count('JACK'))

#
a = []
for i in range(5):
    a.append(input())
print(a)


