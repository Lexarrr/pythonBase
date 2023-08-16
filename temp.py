temperature = 39.8
# alt + numlock 0176 - 30°
string = 'Температура - ' + str(temperature) + '\xB0C'
string += ', это почти ' + str(round(temperature, 0)) + '\xB0C'

print(string)
