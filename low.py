# moduls and their used
# func antagonists
# exception

print('to count % on ten')

num = input('input int: ')

try:
    value = int(num)  # try to do operation / to try string into int
    res = 10 % value
except ZeroDivisionError:
    print(f'you can\'t - 10 / {num} ')  # to write doer except / division on zero
    at_the_end = "no-no-no"
except ValueError:
    print('You have to input int')
    print(f'and you input a: {num}')
    at_the_end = "it's bad!"
except Exception as e:
    print('this is exp:', e.__class__.__name__)
    at_the_end = "And that..."
else:
    print(f'last of division 10 on {value} is {res}')  # if exp not be
    at_the_end = "Thanks"
finally:
    print(at_the_end)  # to do all times
