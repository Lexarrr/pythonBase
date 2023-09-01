# moduls and their used
# func antagonists
# exception

max_value = 10
min_value = 1

try:
    cur_val = int(input(f'input int from {min_value} to {max_value}: '))
    if not min_value <= cur_val <= max_value:
        raise ValueError('input int is not in diapason')
except ValueError as exp:
    print('You must to be attending:', exp)
else:
    print(f'yes. it\'s int exist in this diapason: {min_value}...{max_value}')
