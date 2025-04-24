first_player ,second_player = input().split(', ')

first_player_score = 501
second_player_score = 501


the_matrix = []
for _ in range(7):
    the_matrix.append(input().split())






def get_values(row, col):

    values = 0

    right =  the_matrix[row][-1]
    left = the_matrix[row][0]
    up = the_matrix[0][col]
    down = the_matrix[-1][col]

    values += int(right)
    values += int(left)
    values += int(up)
    values += int(down)



    return values

first_counter = 0
second_counter = 0


counter = 0
current_player = ''


result = ''
while first_player_score > 0 and second_player_score > 0:


    if counter % 2 == 0:
        current_player = first_player
        first_counter += 1
    else:
        current_player = second_player
        second_counter += 1




    info = input()
    row, col = map(int, info[1:-1].split(', '))


    if not (0 <= row < 7 and 0 <= col < 7):
        counter += 1
        continue

    result = the_matrix[row][col]




    if result.isnumeric():
        result = int(result)
        if current_player == first_player:
            first_player_score -= result
        else:
            second_player_score -= result

    if result == 'B':
        if current_player == first_player:
            current_counter = first_counter

        else:
            current_counter = second_counter


        print(f"{current_player} won the game with {current_counter} throws!")
        break
    if result == 'D':
        the_sum = get_values(row,col)
        if current_player == first_player:
            first_player_score -= the_sum * 2
        else:
            second_player_score -= the_sum * 2
    if result == 'T':
        the_sum = get_values(row,col)
        if current_player == first_player:
            first_player_score -= the_sum * 3
        else:
            second_player_score -= the_sum * 3
    counter += 1




if first_player_score <= 0:

    print(f"{current_player} won the game with {first_counter} throws!")
if second_player_score <=0:
    print(f"{current_player} won the game with {second_counter} throws!")














