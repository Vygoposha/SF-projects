a = True
phone_book = {}
while a:
    answer = input(f'Вы хотите создать новую запись в телефонной книге?\n')
    if answer.lower() == 'да':
        name = input('Введите имя:\n')
        phone_num = input('Введите телефонный номер:\n')
        phone_book.update([(name, phone_num)])
        print(phone_book)
    else:
        a = False
print(phone_book)
