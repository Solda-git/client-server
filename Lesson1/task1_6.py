"""

6. Создать программно текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.

Принудительно открыть файл в формате Unicode и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но открыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""
from chardet import UniversalDetector

sequence = ['сетевое программирование', 'сокет', 'декоратор']
FILE_NAME = 'test_file.txt'

with open(FILE_NAME, 'w') as file_descriptor:
    for word in sequence:
        file_descriptor.write(word)
        file_descriptor.write('\n')
file_descriptor.close()

print(f'Determining of encoding of {FILE_NAME}:')
detector = UniversalDetector()
with open(FILE_NAME, 'rb') as file_descriptor:
    for line in file_descriptor:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
file_descriptor.close()

print(detector.result)
encoding = detector.result["encoding"]

print(f'Extracting content of {FILE_NAME}:')
with open(FILE_NAME, 'rb') as file_descriptor:
    for line in file_descriptor:
        print(line.decode(encoding, 'utf-8'), end='')
file_descriptor.close()
