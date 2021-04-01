import redis  #
import json  #

red = redis.Redis(  #
    host="redis-12868.c1.asia-northeast1-1.gce.cloud.redislabs.com",  #
    port=12868,  #
    password="Mnur7otSnKvcPU4XZFiwOhflweNt2g6c"  #
)
# red.set('firstVar','firstValue')  #
# print(red.get('firstVar'))  #
# dict1 = {'key1': 'value1', 'key2': 'value2'}
# red.set('dict1', json.dumps(dict1))  # функцией json.dumps() превратим словарь в строчку
# converted_dict = json.loads(red.get('dict1'))  # c помощью loads прерващаем данные из кеша обратно в словарь
# print(converted_dict, type(converted_dict))
# red.delete('dict1')  # удаляются ключи с помощью метода .delete()
# print(red.get('dict1'
# print(json.loads(red.get('phone_book')))
phone_book = {}
while True:
    first = input(f" Что вы хотите сделать:\n Создать запись в телефоннйо книге?\n Найти телефон по имени?\n"
                  f" Удалить телефон по имени?\n Посмотреть телефонную книгу?\n ")
    if first.lower() == 'создать':
        a = True
        while a:
            answer = input(f'Вы хотите создать новую запись в телефонной книге?\n')
            if answer.lower() == 'да':
                name = input('Введите имя:\n')
                phone_num = input('Введите телефонный номер:\n')
                phone_book.update([(name, phone_num)])
                red.set('phone_book', json.dumps(phone_book))
            else:
                break

    elif first.lower() == 'найти':
        name_find = input(f'Введите имя контакта:\n')
        print(json.loads(red.get('phone_book'))[name_find])
        print()

    elif first.lower() == 'удалить':
        name_del = input('Введите имя, которое нужно удалить из телефонной книги:\n')
        red.delete('phone_book')

    elif first.lower() == 'посмотреть':
        print(json.loads(red.get('phone_book')))
        print()


#"""Пример решений"""
# cont = True
#
# while cont:
#     action = input('action:\t')
#     if action == 'write':
#         name = input('name:\t')
#         phone = input('phone:\t')
#         red.set(name, phone)
#     elif action == 'read':
#         name = input('name:\t')
#         phone = red.get(name)
#         if phone:
#             print(f'{name}\'s phone is {str(phone)}')
#     elif action == 'delete':
#         name = input('name:\t')
#         phone = red.delete(name)
#         if phone:
#             print(f"{name}'s phone is deleted")
#         else:
#             print(f"Not found {name}")
#     elif action == 'stop':
#         break