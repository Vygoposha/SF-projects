import requests
import lxml.html
from lxml import etree

"""Парсинг заголовк, который пишется в названии вкладки"""
# html = requests.get("https://www.python.org/").content  # Получаем HTML указанной страницы целиком
# tree = lxml.html.document_fromstring(html)  #
# title = tree.xpath('/html/head/title/text()')  # забираем текст тега <title> из тега <head>
# # который лежит в свою очередь внутри тега <html>
# # (в этом невидимом теге <head> у нас хранится основная информация о страничке.
# # Её название и инструкции по отображению в браузере.
# print(title)

"""Парсинг из файла HTML"""
# # создадим объект ElementTree. Он возвращается функцией parse()
# tree = etree.parse('Welcome to Python.org.htm', lxml.html.HTMLParser()) #парсим наш файл с помощью html парсера.
# # Сам html - это то что мы скачали и поместили в папку из браузера.
# ul = tree.findall('body/div/div[3]/div/section/div[3]/div[1]/div/ul/li') # помещаем в аргумент методу findall
# # скопированный xpath. Здесь мы получим все элементы списка новостей. (Все заголовки и их даты)
# # из xpath нужно удалить начальный тег /HTML,
# # т.к. для работы метода findall(возвращает список многих подходящих элементов) он не нужен
#
# # в цикле перебираем названия каждого эл-та в xpath
# for li in ul:
#     a = li.find('a') #в каждом элементе находим где хранится заголовок новости. У нас это тег <a>. Т.е.
#     # гиперссылка на которую нужно нажать, чтобы перейти на страницу с новостью.
#     # метод find()возвращает только первый подходящий элемент
#     print(a.text) # из этого тега забираем текст.

"""Задание 5.4.4"""
# html = '''html>
#  <head> <title> Some title </title> </head>
#  <body>
#   <tag1> some text
#      <tag2> MY TEXT </tag2>
#    </tag1>
#  </body>
# </html>'''
#
# tree = lxml.html.document_fromstring(html)  #
# text = tree.xpath('/html/body/tag1/tag2/text()')  # забираем текст тега <title> из тега <head>
# print(text)

"""Задание 5.4.5""" # Парсинг новостей и даты с сайта https://www.python.org
html = requests.get("https://www.python.org/").content  # Получаем HTML указанной страницы целиком
tree = lxml.html.document_fromstring(html)  #
news = tree.xpath('/html/body/div/div[3]/div/section/div[3]/div[1]/div/ul/li')
for li in news:
    a = li.find('a')
    time = li.find('time')
    print('', time.get('datetime'),'\n',a.text)
# for li in news:
#     a = li.find('a')
#     print(a.text)

    # / html / body / div / div[3] / div / section / div[3] / div[1] / div / ul / li[1] / time
