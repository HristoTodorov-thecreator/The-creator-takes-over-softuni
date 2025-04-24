import pyfiglet
fig = pyfiglet.Figlet(font='big')


def check_for_win():
    player_name,player_symbol = players[0]

    first_diag = all([board[i][i] == player_symbol for i in range(size)])
    second_diag = all([board[i][size -1 - i ] == player_symbol for i in range(size)])

    row_win = any([all([pos == player_symbol for pos in row]) for row in board])
    col_win = any([all([board[r][c] == player_symbol for r in range(size)]) for c in range(size)])

    if any([first_diag,second_diag,row_win,col_win]):

        print(fig.renderText(f'{player_name}  -  is the winner'))

        exit()
    players.append(players.pop(0))


def check_for_draw():
    if all([all(pos.strip() for pos in row)for row in board]):
        print(f'Draw!')
        exit()

def place_symbol(position):
    row,col = (position - 1) // size , (position-1) % size # we find the row and the col

    if board[row][col] != ' ':
        raise ValueError

    board[row][col] = players[0][1]
    printboard()

    check_for_win()
    check_for_draw()
    choose_position()




def printboard(begin=False):
    if begin:
        print(f'This is the numeration of the board: ')
        [print(f'| {" | ".join(row)} |') for row in board]
        print(f'{players[0][0]} start first')

        for row in range(size):
            for col in range(size):
                board[row][col] = ' '
    else:
        [print(f'| {" | ".join(row)} |') for row in board]


def choose_position():
    while True:
        try:
            position = int(input(f'{players[0][0]} choose a free position [1-{size * size}]: '))
        except ValueError:
            print(f'Error please choose a number')
            continue

        if 1 <= position <= size * size:
            place_symbol(position)
            break
        else:
            print(f'Error please choose a valid position!')



def start():
    first_player_name = input('First player please choose name: ')
    second_player_name = input('Second player please choose name: ')

    while True:
        first_player_symbol = input(f'{first_player_name} please choose symbol: X OR O - ').upper()

        if first_player_symbol not in ['X','O']:

            print(f'{first_player_name} please select a valid option')

        else:
            break




    second_player_symbol = 'O' if first_player_symbol == 'X' else 'X'
    players.append([first_player_name,first_player_symbol])
    players.append([second_player_name,second_player_symbol])

    printboard(True)
    choose_position()





players = []

board = [[str(i),str(i+1),str(i+2)]for i in range(1,10,3)]


size = len(board)

start()