"""

5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet!!!
"""
import subprocess
from sys import platform
from chardet import detect

RESOURCES = ['yandex.ru', 'youtube.com']
PING_NUMBER = '4'

def ping_resources(system):
    """
    Function starts ping command in OS, provided in param
    :param system: operation system from sys.platform
    :return:
    """
    print(f'Running ping command in system: {system}')
    if platform == 'linux':
        args = ['ping', '-c', PING_NUMBER]
    elif platform == 'win32':
        args = ['ping']
    else:
        print(f'In your system {system} the application not tested')
        args = ['ping', '-c', PING_NUMBER]

    for word in RESOURCES:
        args.append(word)
        process_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in process_ping.stdout:
            output = detect(line)
            print(line.decode(output['encoding'], 'utf-8'), end='')
        args.pop()

ping_resources(platform)
