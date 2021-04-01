field1 = [i for i in range(1,10)]
def show_field_2(field1):
    for i in range(3):
        print(field1[0+i*3], field1[1+i*3], field1[2+i*3])

def player_input(player_var):
    valid = False
    while not valid:
        print('Укажите цифру для записи:')
        answer = input(player_var)
        try:
            answer = int(answer)
        except:
            print("Некорректный ввод, это точно число?")
            continue
        if 1 <= int(answer) <= 9:
            if (str(field1[answer-1]) not in "XO"):
                field1[answer-1] = player_var
                valid = False
            else: print("Клетка уже занята")
        else: print("Некорретный ввод, введите число от 1 до 9")

def win_game(field1):
    var_win = ((0,1,2),
               (3,4,5),
               (6,7,8),
               (0,4,8),
               (1,4,7),
               (2,5,8),
               (0,3,6),
               (2,4,6)
               )
    for i in var_win:
        if field1[i[0]] == field1[i[1]] == field1[i[2]]:
            return field1[i[0]]
    return False

def game_XO(field1):
    counter = 0
    win = False
    while not win:
        show_field_2(field1)
        if counter % 2 == 0:
            player_input("X")
        else:
            player_input("O")
        counter += 1
        if counter > 4:
            tmp = win_game(field1)
            if tmp:
                print(tmp, "выиграл")
                win = True
                break
        if counter == 9:
            print("Ничья!")
            break
    show_field_2(field1)

game_XO(field1)
