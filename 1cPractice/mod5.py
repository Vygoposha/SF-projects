text = ''
inp_str = input("Введите текст: ")
while inp_str:
    text += inp_str
    inp_str = input()
print(text)
unique = set(text)

print("Количество уникальных символов: ", len(unique))
