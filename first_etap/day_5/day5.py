# Напишите проверку на то, является ли строка
# палиндромом.
# Палиндром — это слово или фраза,
# которые одинаково читаются слева направо и справа налево.
# Пример:
# # # тот -> тот
# # # потоп -> потоп
# # # көк -> көк
p = input().lower()
if p == p[::-1]:
    print('Палиндром')
else:
    print('Не палиндром')

# 1
a = 151
while a < 30:
    print(a)

# 2
weather = 'Sunny'
i = 0
while weather == 'Sunny':
    print('Спортсмен пробежал круг')

    i += 1
    if i == 5:
        weather = 'Rainy'
print('Спортсмен идет домой')
print(f'Спортсмен пробежал {i} круг')

# 3
weather = 'Sunny'
i = 0
while True:
    print('Спортсмен пробежал круг')

    i += 1
    if i == 5:
        break
print('Спортсмен идет домой')
print(f'Спортсмен пробежал {i} круг')

# 4

for i in range(10, 25, 2):
    print(i)

# 5

name = 'Python'
for i in range(len(name)):
    print(f'{i} - {name[i]}')

# 6

b = input().lower()
total = 0
for i in b:
    if i == 'а':
        total += 1
print(f'{total} - а в нутри слова {b}')

# 7

a = [1, 'danila', 'dastan', 4, '123']
for i in a:
    print(i)

# problem 1

languaes = ['go']
lang = 'Rist'
for i in languaes:
    if lang == i:
        print('this language is in list')

# problem 4
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in range(len(languages)):
    print(f'{i} - {languages[i]}')

# problem 5
#Напишите цикл который выведет на экран:     1,2,3,4,5,6,7,8,9,10,9,8,7,6,5,4,3,2,1
# Усиление:
# Получите такой же результат но с ОДНИМ циклом
a = ''
for i in range(1, 11):
    a = a + str(i) + ', '

for i in range(9, 0, -1):
    if i == 1:
        a += str(i)
    else:
        a = a + str(i) + ', '
    print(a)

# problem 2
language = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in language:
    if i == 'php':
        break

# problem 3
# Напишите код, который берёт цифру 7, умножает саму на себя же 5 раз.
a = 7
for i in range(5):
    a = a * 7
    print(a)

# problem 6
names = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек','Эрмек', 'Дастан', 'Бекмамат', 'Аслан',)
for i in range(0, len(names), 2):
    print(names[i])

# problem 7
names = ('Максат', 'Лязат', 'Данияр', 'Айбек', 'Атай', 'Салават', 'Адинай', 'Жоомарт', 'Алымбек','Эрмек', 'Дастан', 'Бекмамат', 'Аслан',)

# problem 8 доделать
a = int(input())
if a // 100 != 0 and a > 0 and a%2 ==0 and a % 31 ==0:



# problem 9
t = 0
total1 = 0
for i in range(-100, 101):
    if i % 13 == 0 and i%2==0:
        pass
    if t == 7:
        t = 0
        if i % 2 != 0:
    t += 1


