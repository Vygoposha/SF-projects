import os

def take_way(way = None):
    start_way = way if way is not None else os.getcwd()

    for dirpath, dirnames, filenames in os.walk(start_way):
        for dirname in dirnames:
            print(f"Каталог: {os.path.join(dirpath, dirname)}")
        for filename in filenames:
            print(f'Файл: {os.path.join(dirpath, dirname, filename)}')

take_way(r'C:\Users\iavygolo\PycharmProjects\OOP\C1_Practice\Sea_Battle')


