class Clients:
    def __init__(self, client_name, client_surname=None, balance=None):
        self.client_name = client_name
        self.client_surname = client_surname
        self.balance = balance

    def get_balance(self):
        return (f'Клиент: {self.client_name} {self.client_surname}\n Баланс: {self.balance}')

class Guests(Clients):
    def __init__(self, client_name, city, status):
        super().__init__(client_name)
        # self.client_name = client_name
        self.city = city
        self.status = status

    def get_profile(self):
        return f'Имя {self.client_name}, г.{self.city}, статус {self.status}'

guest_list = []

while True:
    answer = input("Будут ли новые гости?\n")
    if answer == 'нет':
        break
    elif answer == 'да':
        client_name = input('Введите имя:\n')
        city = input('Введите город:\n')
        status = input('Введите статус:\n')
        guest_list.append(Guests(client_name, city, status)) #добавляет в список объект класса Guests
        # print(Guests(client_name, city, status))
    else: print("Введите 'да' или 'нет'")

for i in guest_list:
    print(f'Имя:{i.client_name}, г.{i.city}, статус:{i.status}')
