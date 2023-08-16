a = ['name', 'fio', 'salt', 'app', 'leaf', 'flame', 'fire']

a.sort()

print(a)

for item in a[1:len(a):2]:
    print(item)

for index in range(1, len(a), 2):
    print(a[index])

a1 = []

# a.append(что добавить(значение)

count = 0

for x in reversed(range(11)):
    a1.append(x)
print(a1)

a_b = ['first', 'second']
members = 6

for x in range(members):
    print(a_b[x % len(a_b)])
print('fs')

aa = []

for x in range(11):
    aa.append(x)
print(aa[0:len(a1):2])

aq = list()

for x in range(101):
    if x % 10 == 5:
        aq.append(x)
print(*aq, sep='±')
