def creatematrix(rows,cols):

    matrix = []
    for i in range(rows):
        thecol = cols * [0]
        matrix.append(thecol)

    return matrix


def printmatrix(matrix):

    for i in range(len(matrix)):
        print(matrix[i])






def player_choice(player):
    try:
        choice = int(input(f'Player {player} please choose! - '))

        return choice - 1
    except ValueError:
        print(f'Enter Valid data')




def check_win(matrix, row, col, player, win_counter):
    directions = [
        (0, 1),  # Надясно ➡️
        (0, -1),  # Наляво ⬅️
        (1, 0),  # Надолу ⬇️
        (-1, 0),  # Нагоре ⬆️
        (1, 1),  # Надолу-дясно ↘️
        (-1, -1),  # Нагоре-ляво ↖️
        (1, -1),  # Надолу-ляво ↙️
        (-1, 1)  # Нагоре-дясно ↗️
    ]

    for dr, dc in directions:
        count = 1

        for step in range(1, win_counter):
            new_row, new_col = row + dr * step, col + dc * step

            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                if matrix[new_row][new_col] == 0:  # Ако срещнем 0, прескачаме тази посока
                    continue
                if matrix[new_row][new_col] == player:
                    count += 1
                else:
                    break
            else:
                break

        if count >= win_counter:
            return True

    return False


def main(playground,player_ind,player):
    start = 0

    while start < len(playground) and playground[start][player_ind] == 0:
        start += 1

    if start == 0:
        print(f'You exited the range, next time stay inside the parameters')
        exit()

    playground[start - 1][player_ind] = player

    return start -1,player_ind

def game(matrix,wincounter):
    current_player ,second_player = 1,2

    while True:
        current_player_choice = player_choice(current_player)

        row_ind,col_ind = main(matrix,current_player_choice,current_player)


        if check_win(matrix, row_ind, col_ind, current_player, win_counter):
            print(f'Player {current_player} wins!')
            printmatrix(matrix)
            break  # Край на играта
        printmatrix(matrix)




        current_player,second_player = second_player,current_player


try:
    rows = int(input('Enter rows:'))
    columns = int(input('Enter Columns'))
    win_counter = int(input('Enter number for win combination'))

    matrix = creatematrix(rows, columns)
    game(matrix, win_counter)



except ValueError:
    print(f'Enter valid data')














