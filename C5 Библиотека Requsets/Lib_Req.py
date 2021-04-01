import requests
import json  # импортируем необходимую библиотеку
from requests.exceptions import HTTPError

# r = requests.get('https://baconipsum.com/api/?type=meat-and-filler')
# texts = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
# print(type(texts))  # проверяем тип сконвертированных данных
#
# for text in texts:  # выводим полученный текст. Но для того чтобы он влез в консоль оставим только первые 50 символов.
#     print(text[:50], '\n')

###
# r = requests.get('https://api.github.com')
#
# d = json.loads(r.content)  # делаем из полученных байтов python объект для удобной работы
#
# print(type(d))
# print(d['following_url'])  # обращаемся к полученному объекту как к словарю и попробуем напечатать одно из его значений

###
    # r = requests.post('https://httpbin.org/post', data = {'key':'value'}) # отправляем пост запрос
    # print(r.content) # содержимое ответа и его обработка происходит также как и с ГЕТ запросами, разницы никакой нету

###
# data = {'key': 'value'}
#
# r = requests.post('https://httpbin.org/post', json=json.dumps(
#     data))  # отправляем пост запрос, но только в этот раз тип передаваемых данных будет JSON
# print(r.content)


# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#
#         # если ответ успешен, исключения задействованы не будут
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')


# r = requests.get('https://api.github.com/')
# status = r.status_code
# cont = r.content
# print(cont, '\n', type(cont))  # Вывод в виде байтов, полученных в запросе
# text = r.text
# print((text, '\n', type(text))) # Вывод в виде текста, полученных в запросе
# Если необходимо использовать определнную кодировку:
# r.encoding = 'utf-8'
# print(r.text)
# js_on = (r.json()) # Данные в формате словаря JSON\
# print(js_on)
# print(js_on.keys()) #можно применять методы словарей
# print(r.headers['content-type'])  # HTTP заголовки, формат:словарь, не чувствительный к


"""Python Requests параметры запроса"""
# Поиск местонахождения для запросов на GitHub
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'}, #второй аргемент get запроса в формате словаря/кортежа/байтов
# )
#
# # Анализ некоторых атрибутов местонахождения запросов
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Repository name: {repository["name"]}')  # Python 3.6+
# print(f'Repository description: {repository["description"]}')  # Python 3.6+

"""Настройка HTTP заголовка запроса (headers)"""
# response = requests.get(
#     'https://api.github.com/search/repositories',
#     params={'q': 'requests+language:python'},
#     headers={'Accept': 'application/vnd.github.v3.text-match+json'},
# )
# #Заголовок Accept сообщает серверу о типах контента, который можно использовать в рассматриваемом приложении.
#
# # просмотр нового массива `text-matches` с предоставленными данными
# # о поиске в пределах результатов
# json_response = response.json()
# repository = json_response['items'][0]
# print(f'Text matches: {repository["text_matches"]}')

"""Задание 5.2.3"""

# r = requests.get("https://baconipsum.com/api/?type=all-meat&paras=3&start-with-lorem=1&format=htm")
# r = json.loads(r.text)
# print(r[0])
# c = r.text
# r.encoding = 'utf-8'
# print(c)

# r = requests.get("https://api.exchangeratesapi.io/latest")
# print(r.content)
s = requests.get('https://api.exchangeratesapi.io/latest?baseUSD&symbols=RUB')
print(s.content)
# x = json.loads(s.content)
# print(x)
# print(x['rates']['RUB'])
# print(x['base'])
# print(x['date'])
# print(json.loads(s.content)['rates']['RUB'])
# print((json.loads(s.content)).keys())
# print((json.loads(s.content))['rates'].keys())

# g = requests.get('https://api.exchangeratesapi.io/latest')
# print(g.content)