num = input("Введите число:")
try:
    num = int(num)
except ValueError as e:
    print("Вы ввели неправильное число")
else:
    print(f"Вы ввели число {num}")
finally:
    print("Выход из программы")