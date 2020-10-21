"""

4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

DEVELOPMENT = "разработка"
ADMINISTRATION = "администрирование"
PROTOCOL = "protocol"
STANDARD = "standard"

sequence = [DEVELOPMENT, ADMINISTRATION, PROTOCOL, STANDARD]
sequence_encoded = []
sequence_decoded = []
for word in sequence:
    ENCODED = word.encode('utf-8')
    sequence_encoded.append(ENCODED)
    sequence_decoded.append(ENCODED.decode('utf-8'))

print(f'Байтовое представление: {sequence_encoded}')
print(f'Декодированная последовательность: {sequence_decoded}')
