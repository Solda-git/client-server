"""

1. Каждое из слов «разработка», «сокет», «декоратор» представить
в буквенном формате и проверить тип и содержание соответствующих переменных.
Затем с помощью онлайн-конвертера преобразовать
в набор кодовых точек Unicode и также проверить тип и содержимое переменных.

Подсказки:
--- 'разработка' - буквенный формат
--- '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430' - набор кодовых точек
--- используйте списки и циклы, не дублируйте функции
"""

DEVELOPMENT1 = 'разработка'
SOCKET1 = 'сокет'
DECORATOR1 = 'декоратор'

DEVELOPMENT2 = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
SOCKET2 = '\u0441\u043e\u043a\u0435\u0442'
DECORATOR2 = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

def dump(arr):
    """
    Prints info about arr items: value and type
    :param arr:
    :return:
    """
    for i in arr:
        print(f'Сожержимое: {i}, тип: {type(i)}')

sequence = [DEVELOPMENT1, SOCKET1, DECORATOR1]
dump(sequence)

sequence = [DEVELOPMENT2, SOCKET2, DECORATOR2]
dump(sequence)
