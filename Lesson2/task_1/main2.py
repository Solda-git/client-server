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
import csv
import re
import yaml
from chardet import UniversalDetector

FILES = ['info_1.txt', 'info_2.txt', 'info_3.txt']
FIELDS = [
    'Изготовитель системы',
    'Название ОС',
    'Код продукта',
    'Тип системы'
]

OUTPUT_FILE = 'my_data_report.csv'
def get_encoding(_file):
    """
    function defines encoding of file in param
    :param _file:
    :return: encoding
    """
    print('Detecting encoding...')
    detector = UniversalDetector()
    with open(_file, 'rb') as file_descriptor:
        for line in file_descriptor:
            detector.feed(line)
            if detector.done:
                break
        detector.close()
    file_descriptor.close()
    encoding = detector.result["encoding"]
    print('Detected encoding:', encoding)
    return encoding

# building PATTERN of needed fields to be logged
PATTERN = ''
for index, field in enumerate(FIELDS):
    PATTERN += f'({field})'
    if index < len(FIELDS) - 1:
        PATTERN += '|'
regex = re.compile(PATTERN)
# print(f'Pattern: {regex}')

obj_list = []
COUNTER = 0
for file in FILES:
    with open(file, mode='r', encoding=get_encoding('info_1.txt')) as file_txt:
        COUNTER += 1
        obj_string = f"Номер: {str(COUNTER)}\n"
        for record in file_txt.readlines():
            result = regex.match(record)
            if result:
                obj_string += record
        obj_list.append(yaml.load(obj_string, Loader=yaml.FullLoader))
    file_txt.close()
print(obj_list)
print(obj_list[0])
print(obj_list[0].keys())
print(obj_list[0].values())

with open(OUTPUT_FILE, mode='w',  encoding='utf-8') as file_csv:
    file_writer = csv.DictWriter(file_csv,
                                 delimiter=';',
                                 fieldnames=obj_list[0].keys()
                                 )
    file_writer.writeheader()
    for obj in obj_list:
        file_writer.writerow(obj)
file_csv.close()
