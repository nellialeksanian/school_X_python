player_1, player_2 = input('Ввод: ').split(' ')
if player_1 == player_2:
    print("Ничья")
elif player_1 == 'камень':
    if player_2 =='ножницы':
        print("Выиграл первый игрок")
    else:
        print("Выиграл второй игрок")
elif player_1 == 'ножницы':
    if player_2 =='бумага':
        print("Выиграл первый игрок")
    else:
        print("Выиграл второй игрок")
else:
    if player_2 =='камень':
        print("Выиграл первый игрок")
    else:
        print("Выиграл второй игрок")
