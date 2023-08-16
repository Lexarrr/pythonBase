a = ['name', 'fio', 'salt', 'app', 'leaf', 'flame', 'fire']

a.sort()

print(a)

for item in a[1:len(a):2]:
    print(item)

for index in range(1, len(a), 2):
    print(a[index])
