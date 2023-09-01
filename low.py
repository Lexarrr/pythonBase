# method find(substr, start = 0, end =none)
# method replace(old, new, count = none)

string = '+7-921-266-02-11'
length = len(string)

# replace - on space
c_bracket_phone = string.replace('-', ' ')
print(c_bracket_phone)

# replace on open brackets
c_bracket_phone = string.replace('-', ' (', 1)
print(c_bracket_phone)

# replace on close brackets
c_bracket_phone = string.replace('-', ') ', 1) # ???????????????????????????????????????????????
print(c_bracket_phone)
