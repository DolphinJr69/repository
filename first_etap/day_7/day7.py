# name = {'dastan', 'danila', 'sonun', 'roman'}
# print(name)


# name = {'dastan', 'danila', 'sonun', 'roman'}
# name2 = {'abdymazhit', 'natalia', 'dastan', 'nuriza'}
# print(name.difference(name2))


# name = {'dastan', 'danila', 'sonun', 'roman'}
# name2 = {'abdymazhit', 'natalia', 'dastan', 'nuriza'}
# name.remove('roman')
# print(name)


# name = {'dastan', 'danila', 'sonun', 'roman'}
# name2 = {'abdymazhit', 'natalia', 'dastan', 'nuriza'}
# name.discard('roman')
# print(name)


# name = {'dastan', 'danila', 'sonun', 'roman'}
# name2 = {'abdymazhit', 'natalia', 'dastan', 'nuriza'}
# name.intersection_update(name2)
# print(name)


# name = {'dastan', 'danila', 'sonun', 'roman'}
# name2 = {'abdymazhit', 'natalia', 'dastan', 'nuriza'}
# print(name.pop())


##############################################################

# data = {
#     "name": 'Dastan',
#     "last_name": 'Kybanov',
#     "age": 19,
#     "stacks": ['Python', 'C++', 'UE4'],
#     "laptop":{
#         'name': 'macbook',
#         'year': 2017,
#         'cost': 60000
#     }
# }
# print(data['name'], data['age'])


# data = {
#     "name": 'Dastan',
#     "last_name": 'Kybanov',
#     "age": 19,
#     "stacks": ['Python', 'C++', 'UE4'],
#     "laptop":{
#         'name': 'macbook',
#         'year': 2017,
#         'cost': 60000
#     }
# }
# print(data['name'], data['age'])
# for i in data['stacks']:
#     print(i)


# data = {
#     "name": 'Dastan',
#     "last_name": 'Kybanov',
#     "age": 19,
#     "stacks": ['Python', 'C++', 'UE4'],
#     "laptop": {
#         'name': 'macbook',
#         'year': 2017,
#         'cost': 60000
#     }
# }
# data['name'] = input()
# data['stacks'] = input()
#
# print(data)
#HASH ТАБЛИЦА ВЫШЕ


# data = {
#     "name": 'Dastan',
#     "last_name": 'Kybanov',
#     "age": 19,
#     "stacks": ['Python', 'C++', 'UE4'],
#     "laptop": {
#         'name': 'macbook',
#         'year': 2017,
#         'cost': 60000
#     }
# }
# data['name'] = input()
# data['stacks'] = input()
#
# for i in data.keys():
#     print(data[i])


# data = {
#     "name": 'Dastan',
#     "last_name": 'Kybanov',
#     "age": 19,
#     "stacks": ['Python', 'C++', 'UE4'],
#     "laptop": {
#         'name': 'macbook',
#         'year': 2017,
#         'cost': 60000
#     }
# }
#
# for i, j in data.items():
#     print(f'{i}, - {j}')


# data = {
#     "name": 'Dastan',
#     "last_name": 'Kybanov',
#     "age": 19,
#     "stacks": ['Python', 'C++', 'UE4'],
#     "laptop": {
#         'name': 'macbook',
#         'year': 2017,
#         'cost': 60000
#     }
# }
#
# data.update({'name': 'danila'})
# print(data)


######################################################


# a = [('abdymazit', 'danila'), ('erkinbel', 'natalia'), ('nuriza', 'roma',), ('saltanat', 'sonun')]
# for i in a:
#     print(i)


# a = [('abdymazit', 'danila'), ('erkinbel', 'natalia'), ('nuriza', 'roma',), ('saltanat', 'sonun')]
# for i, j in a:
#     print(i, j)


# PROBLEM 10

# menu = {'lagman': 120, 'plov': '120', 'borsh': 100}
# menu['Drinks'] = ['Coca-Cola', 'Sprite', 'Fanta']
# print(menu)

#
# a = ['234', 'qwerty', '234', '543', 'qwerty']
# b = set(a)
# a = list(b)
# print(a)


# PROBLEM 020
# numbers = {'.add', '.remove', '.clear', '.update', '.difference', '.discard', '.intersection', '.intersection_update', '.pop'}
# numbers2 = {'.clear', '.keys', '.get', '.values', '.items', '.items', '.update'}
# print(numbers.difference(numbers2))

# PROBLEM 31
a = {

}
for i in range(3):
   username = input()
   password = input()
   a[username] = password
   print(a)

# PROBLEM 27