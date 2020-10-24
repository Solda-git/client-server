
"""
2. Задание на закрепление знаний по модулю json. Есть файл orders
в формате JSON с информацией о заказах. Написать скрипт, автоматизирующий
его заполнение данными.

Для этого:
Создать функцию write_order_to_json(), в которую передается
5 параметров — товар (item), количество (quantity), цена (price),
покупатель (buyer), дата (date). Функция должна предусматривать запись
данных в виде словаря в файл orders.json. При записи данных указать
величину отступа в 4 пробельных символа;
Проверить работу программы через вызов функции write_order_to_json()
с передачей в нее значений каждого параметра.

ПРОШУ ВАС НЕ УДАЛЯТЬ ИСХОДНЫЙ JSON-ФАЙЛ
ПРИМЕР ТОГО, ЧТО ДОЛЖНО ПОЛУЧИТЬСЯ

{
    "orders": [
        {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        },
        {
            "item": "scaner",
            "quantity": "20",
            "price": "10000",
            "buyer": "Petrov P.P.",
            "date": "11.01.2018"
        }
    ]
}

вам нужно подгрузить JSON-объект
и достучаться до списка, который и нужно пополнять
а потом сохранять все в файл
"""
import json

ITEM0 = {
            "item": "notebook",
            "quantity": "1",
            "price": "100000",
            "buyer": "Soldatov S.",
            "date": "24.10.2020"
        }

ITEM1 = {
            "item": "printer",
            "quantity": "10",
            "price": "6700",
            "buyer": "Ivanov I.I.",
            "date": "24.09.2017"
        }

JSON_FILE = 'orders.json'

def write_order_to_json(_item, _quantity, _price, _buyer, _date):
    """
    Function adds cart_item with params in the cart file 'orders.json'
    :param _item:
    :param _quantity:
    :param _price:
    :param _buyer:
    :param _date:
    :return:
    """
    # content = {}
    cart_item = {
            "item": _item,
            "quantity": _quantity,
            "price": _price,
            "buyer": _buyer,
            "date": _date
        }
    print(cart_item)
    with open(JSON_FILE, mode='r') as file_read:
        content = json.load(file_read)
        print(f"content: {content}")
    file_read.close()

    content['orders'].append(cart_item)

    with open(JSON_FILE, mode='w', encoding='utf-8') as file_write:
        json.dump(content, file_write)
    file_write.close()

write_order_to_json(ITEM0["item"], ITEM0["quantity"], ITEM0["price"], ITEM0["buyer"], ITEM0["date"])
write_order_to_json(ITEM1["item"], ITEM1["quantity"], ITEM1["price"], ITEM1["buyer"], ITEM1["date"])
