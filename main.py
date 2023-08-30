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

# ram randon access memory
# ssd solid state drive
# filename + . ext - expansion
# a (append) - ++

f = open('info.text', 'rt', encoding='utf-8')
bytes = f.write('it\'s very annoying and bored, i can\'t to hear it\n')
print(bytes)
f.close()
