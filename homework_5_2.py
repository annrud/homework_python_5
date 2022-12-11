import random

number_of_candies = 2021
max_player_turn = 28
min_player_turn = 1

print(f'''
Игра с конфетами. Условие задачи: На столе лежит {number_of_candies} конфета.
Играют два игрока делая ход друг после друга.
Первый ход определяется жеребьёвкой.
За один ход можно забрать не более чем {max_player_turn} конфет.
Все конфеты оппонента достаются сделавшему последний ход.
Для прерывания игры нажмите 0.
'''
      )


def play(max_candies, min_candies, amount, bot, winner=None):
    first_turn = amount % (max_candies + min_candies)
    if bot == 'n':
        first_player_name = input('Введите имя первого игрока: ')
        second_player_name = input('Введите имя второго игрока: ')
    else:
        first_player_name = input('Введите своё имя: ')
        second_player_name = 'bot'
    first = first_player_name
    second = second_player_name
    rand = random.randint(1, 2)
    if rand == 2:
        first, second = second_player_name, first_player_name
    print(f'По результату рандомного выбора первым ходить будет игрок {first}')
    cnt = 0
    while True:
        if amount == 0:
            break
        if first != 'bot':
            cnt = input(f'{first}, введите сколько конфет вы берёте: ')
            if cnt.isdigit():
                cnt = int(cnt)
                if cnt == 0:
                    print('Прерывание игры!')
                    winner = None
                    break
                elif cnt < min_candies or cnt > max_candies:
                    print(f'{first}, число конфет должно быть от {min_candies} до {max_candies} за ход!')
                    continue
                if amount < cnt:
                    print(f'{first}, вы не можете взять более {amount} конфет!')
                    continue
            else:
                print('Неправильный ввод!')
                continue
        else:
            if first_turn:
                cnt = first_turn
                first_turn = 0
            else:
                cnt = (max_candies + min_candies) - cnt
            print(f'bot: Беру {cnt} конфет')
        amount -= cnt
        winner = first
        first, second = second, first
        print(f'Конфет осталось {amount} штук')
    return f'Победил {winner}!'


while True:
    choice = input('Напишите "y", если вы будете играть с ботом и "n", если вы будете играть в паре: ')
    if choice == '0':
        print('Прерывание игры!')
        break
    elif choice == 'y' or choice == 'n':
        print(
            play(
                max_candies=max_player_turn,
                min_candies=min_player_turn,
                amount=number_of_candies,
                bot=choice
            )
        )
        break
    else:
        print('Неверный ввод!')
        continue
