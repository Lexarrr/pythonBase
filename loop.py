count = 3
password = '123'
userword = ''

while True:
    userchoice = input('Введите пароль: ')
    if password == userchoice:
        print('Доступ разрешен')
        break
    count -= 1

    if count == 0:
        print('Попытки исчерпаны')
        break
    else:
        print('Пароль неверный. повторите попыток осталось - ' + str(count))

# пропуск шага ++ - continue
