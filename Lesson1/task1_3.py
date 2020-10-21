"""

3. Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b'' (без encode decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- усложните задачу, "отловив" и обработав исключение

"""
ATTRIBUTE = "attribute"
CLASS = "класс"
FUNCTION = "функция"
TYPE = "type"
sequence = [ATTRIBUTE, CLASS, FUNCTION, TYPE]

def no_convertable_to_byte(arr):
    """
    Function determines non convertable strings to bytes format
    :param arr:
    :return:
    """
    result = []
    for word in arr:
        for symbol in word:
            if ord(symbol) > 255:
                result.append(word)
                break
    return result


print(f'Не могут быть преобразованы к байтам следующие слова: {no_convertable_to_byte(sequence)}.')


def no_convertable_to_byte2(arr):
    """
    Function determines non convertable strings to bytes format with
    exception handling
    :param arr:
    :return:
    """
    result = []
    for word in arr:
        try:
            bytes(word, 'ASCII')
        except UnicodeEncodeError as exception:
            print(f'Ошибка преобразования для слова "{word}": {exception}')
            result.append(word)
    return result

print(f'Вариант 2: {no_convertable_to_byte2(sequence)}.')
