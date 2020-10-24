"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""
import yaml

YAML_FILE = 'my.yaml'

SOLDATA = {
    'foods': ['carrot', 'apple', 'onion', 'tomato'],
    'number': 42,
    'pointers': {
        'Челябинск': '1480\u261B',
        'Череповец': '370\u261D',
        'Новороссийск': '1220\u261F'
    }
}

def write_to_yaml(_file, _object):
    """
    Function writes data in yaml file
    :param _file:
    :param _object:
    :return:
    """
    with open(_file, 'w', encoding='utf-8') as file_write:
        yaml.dump(_object,
                  file_write,
                  default_flow_style=False,
                  allow_unicode=True,
                  encoding='utf-8'
                  )
    file_write.close()

def read_from_yaml(_file):
    """
    Function reads data from yaml file and prints the content
    :param _file:
    :return:
    """
    with open(_file, 'r', encoding='utf-8') as file_read:
        print(yaml.load(file_read, Loader=yaml.FullLoader))
    file_read.close()

#__maoin()__
print(f'Начальное содержание словаря: {SOLDATA}')
write_to_yaml(YAML_FILE, SOLDATA)
print('Данные записаны в файл. Содержание после извлечения:')
read_from_yaml(YAML_FILE)
