from bs4 import BeautifulSoup
import requests
import fake_useragent

user = fake_useragent.UserAgent().random
header = {'user-agent': user}
print(user)

link = 'https://ru.stackoverflow.com/'  # ссылка на сайт, откуда будем парсить
html = requests.get(link, headers = header).content  # запрос html кода страницы в байтаовом виде
status = requests.get(link).status_code
print(f'Статус код сервера: {requests.get(link).status_code}\n')
soup = BeautifulSoup(html, 'lxml')  # создаем объект библиотеки BS, 1ый арг - html-код, 2ой - библиотека париснга
div = soup.find('div', id="question-mini-list")  # находим методом find нужный нам контейнер/div
a = div.find_all('a', class_="question-hyperlink")  # ищем объекты с тегом <a и классом class="question-hyperlink
# parent = a.find_parent() # находим первого родителя тега a, перменять find_all на find
# print(parent)
# find_all возвращает список объектов bs, котоыре удовлетворяют условиям поиска
# file = open('stacklink.doc', 'w')
if status == 200:
    for _ in a:  # итерируемяся по списку а
        print(_.text,'\n', link + _.get('href')) # находим методом getText() текст ссылки, можно просто .text
        # а методом get('href')
        # саму ссылку. т.к. ссылка относительная отнсительно link, то прибавлем его.
        # file.write(f'{_.text}\n\n{link + _.get("href")}\n\n')
else: print(f'Что-то не так, код отвта от сервера: {status}')
