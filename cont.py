list_ = ['яблоки', 'картофель', 'морковь', 'свекла']
print(f'Я должен купить {len(list_)} продуктов')
for product in list_:
    print(product, end="")
print()
list_.append('чипсы')
# list_.sort()
# list_.reverse()
list_ = sorted(list_, reverse=True)
print(list_)
data = [123, 123, 5.3, True]
print(data)
s = 123
print(list((1, 2, 3)))
data.append('5')
data.extend([6, 7, 8])
print(data)
print(data.count(123))
# print(data.index(123, 1, 5))
data.insert(1, 555)
print(data)
data.remove(5.3)
print(data)
data.clear()
data_ = []
for i in range(1, 11):
    data_.append(i - 1)
print(data_)

data_ = [x ** 2 for x in range(1, 11) if x % 2 == 0]  # берем из последовательности (1, 10) x и используем x
print(data_)
