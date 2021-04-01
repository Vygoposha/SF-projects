field = [['-'] * 3 for i in range(3)]

def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: yx ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
    print("-------------------")
    print(" ")

def show_field():
    print(f'  0 1 2')
    for i in range(3):
        print(f'{i} {field[i][0]} {field[i][1]} {field[i][2]}')


def user_choice():
    while True:
        print('Укажите координату для записи:')
        answer = input()
        if len(answer) == 2:
            try:
                x, y = int(answer[0]), int(answer[1])
            except:
                print("Некорректный ввод, это точно число?")
                continue
            if 0 <= x <= 2 and 0 <= y <= 2:
                print(x, y)
                if field[x][y] != "-":
                    print(" Клетка занята! ")
                    show_field()
                    continue
            else:
                print("Число вне диапазона координат")
                continue
            return x, y
        else:print("Значение координаты должно состоять из двух цифр")


def win_game():
    var_win = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for i in var_win:
        a = i[0]
        b = i[1]
        c = i[2]

        if field[a[0]][a[1]] == field[b[0]][b[1]] == field[c[0]][c[1]] != "-":
            return True
    return False


def game():
    greet()
    counter = 0
    while True:
        counter += 1
        show_field()
        if counter % 2 == 0:
            print("Ход ноликов")
        else:
            print("Ход крестиков")
        x, y = user_choice()
        if counter % 2 == 1:
            field[x][y] = "X"
        else:
            field[x][y] = "O"
        if win_game():
            print(f"Победили {field[x][y]}")
            show_field()
            break
        if counter == 9:
            print("Ничья!")
            break
        print(f"Число ходов {counter}")


game()