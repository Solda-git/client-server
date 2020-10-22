"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import json
import re

import yaml
from chardet import UniversalDetector

FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
FIELDS = ['Изготовитель системы','Название ОС','Код продукта','Тип системы']

OUTPUT_FILE = 'my_data_report.csv'
#
def get_encoding(_file):
    print(f'Determining of encoding of {_file}:')
    detector = UniversalDetector()
    with open(_file, 'rb') as file_descriptor:
        for line in file_descriptor:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    file_descriptor.close()
    return detector.result["encoding"]
#
# def produce_csv_file(FILES, _encoding):
#     for f in FILES:
#         with open(f, mode='r', encoding=_encoding) as file_descriptor:
#             pass
#
pattern = ''
for index, field in enumerate(FIELDS):
    pattern += f'({field})'
    if index < len(FIELDS) - 1:
        pattern += '|'

regex = re.compile(pattern)

obj = {}

obj_list = []

for file in FILES:
    with open(file, mode='r', encoding=get_encoding('info_1.txt')) as file_descriptor:
        obj_string = ""
        for line in file_descriptor.readlines():
            # print(line)
            result = regex.match(line)
            if result:
                print(line, end='')
            if result:
                obj_string += line
        obj_list.append(yaml.load(obj_string, Loader=yaml.FullLoader))
    file_descriptor.close()
print(obj_list)