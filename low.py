# moduls and their used
# func antagonists
# exception
# Assertion

try:
    text = input('input any text: ')
    assert len(text) > 3
except AssertionError:
    print('Length of text smallest then 3 symbols')
