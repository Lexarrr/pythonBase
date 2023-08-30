def smart_greeting(hour):
    if 12 < hour <= 7:
        return 'Доброе утро!'
    if 18 < hour <= 12:
        return 'Добрый день!'
    if 18 < hour <= 12:
        return 'Добрый вечер!'
    return 'Добрый ночи!'
