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

class FileParser:

    def __init__(self, _file_list, _field_list):
        self.file_list = _file_list
        self.field_list = _field_list
        self.object_list = []
        _pattern = ''
        for index, field in enumerate(self.field_list):
            _pattern += f'({field})'
            if index < len(self.field_list) - 1:
                _pattern += '|'
        self.pattern = re.compile(_pattern)

    def __str__(self):
        return f'file_list: {self.file_list}\n' \
               f'field_list: {self.field_list}\n' \
               f'pattern: {self.pattern}\n' \
               f'object_list: {self.object_list}\n'

    def get_encoding(self, _file):
        """
        function defines encoding of file in param
        :param _file:
        :return: encoding
        """
        print(f'Detecting file: {_file}...')
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

    def get_data(self):
        counter = 0
        # collecting data from txt file in common dictionary
        for file in self.file_list:
            with open(file, mode='r', encoding=self.get_encoding(file)) as file_txt:
                counter += 1
                obj_string = f"Номер: {str(counter)}\n"
                for record in file_txt.readlines():
                    if self.pattern.match(record):
                        obj_string += record
                self.object_list.append(yaml.load(obj_string, Loader=yaml.FullLoader))
            file_txt.close()
        # print(obj_list)
        # forming service arrays

    def write_to_csv(self, _csv_file):
        with open(_csv_file, mode='w', encoding='utf-8') as file_csv:
            file_writer = csv.DictWriter(file_csv,
                                         delimiter=';',
                                         fieldnames=self.object_list[0].keys()
                                         )
            file_writer.writeheader()
            for obj in self.object_list:
                file_writer.writerow(obj)
        file_csv.close()


# __main()__
parser = FileParser(FILES, FIELDS)
# print(parser)
parser.get_data()
# print(parser)
parser.write_to_csv(OUTPUT_FILE)

#
#
# # building PATTERN of needed fields to be logged
# PATTERN = ''
# for index, field in enumerate(FIELDS):
#     PATTERN += f'({field})'
#     if index < len(FIELDS) - 1:
#         PATTERN += '|'
# regex = re.compile(PATTERN)
#
# obj_list = []
# COUNTER = 0
# for file in FILES:
#     with open(file, mode='r', encoding=get_encoding('info_1.txt')) as file_txt:
#         COUNTER += 1
#         obj_string = f"Номер: {str(COUNTER)}\n"
#         for record in file_txt.readlines():
#             result = regex.match(record)
#             if result:
#                 obj_string += record
#         obj_list.append(yaml.load(obj_string, Loader=yaml.FullLoader))
#     file_txt.close()
#
# print(obj_list[0].keys())
#
# with open(OUTPUT_FILE, mode='w',  encoding='utf-8') as file_csv:
#     file_writer = csv.DictWriter(file_csv,
#                                  delimiter=';',
#                                  fieldnames=obj_list[0].keys()
#                                  )
#     file_writer.writeheader()
#     for obj in obj_list:
#         file_writer.writerow(obj)
# file_csv.close()
