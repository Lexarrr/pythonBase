# method find(substr, start = 0, end =none)

string = 'watching, listening, seeing'

# if string.find('ing') != -1:
if 'ing' in string:
    count = string.count('ing')

    print('"ing" to finds', count, 'times')

    index = string.find('ing')  # from first symb(index) / start
    print(index)

    index = string.find('ing', index + 1)  # from any index
    print(index)

    length = len(string)

    index = string.find('ing', index + 1, length)  # from any index
    print(index)
else:
    print('not find')
