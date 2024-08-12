
first_name = input()
second_name = input()

first_player_points = 0
second_player_points = 0

while True:
    command_ = input()
    if command_ == 'End of game':
        print(f'{first_name} has {first_player_points} points')
        print(f'{second_name} has {second_player_points} points')
        break
    first_player = int(command_)
    seconds_player = int(input())


    if first_player > seconds_player:
        first_player_points =first_player_points + first_player - seconds_player
    elif seconds_player > first_player:
        second_player_points = second_player_points + seconds_player - first_player

    elif seconds_player == first_player:
        print(f'Number wars!')
        first_player = int(input())
        seconds_player = int(input())


        if first_player > seconds_player:
             print(f"{first_name} is winner with {first_player_points} points")
             break
        elif seconds_player > first_player:
            print(f'{second_name} is winner with {second_player_points} points')
            break


