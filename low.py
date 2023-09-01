# moduls and their used
# func antagonists
# exception

n = 3
a = [1, 2]

if n <= 3:
    name = 'Sandra'
try:
    # print(name)
    # print(a[5])
    with open('inf.text') as f:
        print(f.read())
except Exception as exp:
    print('and name exception:', exp.__class__.__name__)
# except NameError:
#     print('not defined name')
# except IndexError:
#     print('index out of range')
# except FileNotFoundError:
#     print(' not find file name')

