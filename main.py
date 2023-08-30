# def smart_greeting(hour):
#     if 12 < hour <= 7:
#         return 'Доброе утро!'
#     if 18 < hour <= 12:
#         return 'Добрый день!'
#     if 23 < hour <= 18:
#         return 'Добрый вечер!'
#
#
# print(smart_greeting(7))
import os

print('hear', end=' -> ')
print(os.getcwd()) # action directory
print(os.chdir('..')) # new path to directory
print('and now hear', end=' -> ')
print(os.getcwd())

# ram randon access memory
# ssd solid state drive
# filename + . ext - expansion
# mode - w create or delete and write again
# a (append) - ++
#
# f = open('info.text', 'at', encoding='utf-8')
# bytes = f.write('it\'s very annoying and bored, i can\'t to hear it\n')
# print(bytes)
# f.close()
#
# f = open('info.text', 'rt', encoding='utf-8')
# info = f.read(5)
# print(info)
# f.read(36)
# info = f.read(10)
# print(info)
# f.close()

# f = open('info.text', 'rt', encoding='utf-8')
# # lin = f.read(4)
# # lin = f.read(6)
# for _ in range(2):
#     f.readline()
# line = f.readline()
# print(line)
#
# f.close()


list_1 = [1, 3, 5, 8, 12, 24, 37, 55, 89]
list_2 = [2, 4, 5, 8, 14, 24, 39, 58, 89]

result = set(list_1) & set(list_2)  # пересечение
# set1.intersection(set2)

# менеджер контекста
# отвечает за автоматическое закрытие файла
with open('info.text', 'w') as f:
    print(*sorted(result), sep=', ', file=f)


