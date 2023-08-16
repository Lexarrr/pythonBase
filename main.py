# списки

array = []  # void array
array2 = list()  # void array from func list
array3 = [1, 2, 3, 4, 5, 6]
list_4 = [36.6, 50, 'Temperature', False]
array5 = list('Python')  # void array from func list
index = -1
length = len(list_4)
# print('array\'s length - ', length)
# print(list_4[index])

counter = 0

while counter < len(list_4):
    print(list_4[counter])
    counter += 1

# slice depend sys sss
# start(include), defalt - null
# stop (uninc)
# step, def - 1

print(list_4[0:len(list_4):2])

a = ['name', 'fio', 'salt', 'app', 'leaf', 'flame', 'fire']
print(a[4:])
