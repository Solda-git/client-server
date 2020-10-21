"""

2. Каждое из слов «class», «function», «method» записать в байтовом формате
без преобразования в последовательность кодов
не используя методы encode и decode)
и определить тип, содержимое и длину соответствующих переменных.

Подсказки:
--- b'class' - используйте маркировку b''
--- используйте списки и циклы, не дублируйте функции
"""

from sys import getsizeof

CLASS = b"class"
FUNCTION = b"function"
METHOD = b"method"
DELIMETER = '_'*43

sequence = [CLASS, FUNCTION, METHOD]
print('тип\t\t\t\tсодержание\tдлина\tразмер')
for i in sequence:
    print(DELIMETER)
    print(f'{type(i)}\t{i}\t{len(i)}\t\t{getsizeof(i)}')
print(DELIMETER)
