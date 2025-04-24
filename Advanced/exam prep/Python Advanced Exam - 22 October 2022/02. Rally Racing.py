size_matrix = int(input())
number_of_car = input()

row,col = 0,0
matrix = []
kms = 0
for i in range(size_matrix):
    race_route = input().split()
    matrix.append(race_route)

directions = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

while True:
    command = input()

    if command == "End":
        print(f"Racing car {number_of_car} DNF.")
        break

    the_move = directions[command]
    new_row,new_col = row + the_move[0] , col + the_move[1]

    if matrix[new_row][new_col] == '.':
        kms += 10
        row, col = new_row, new_col
    elif matrix[new_row][new_col] == 'F':
        kms += 10
        print(f"Racing car {number_of_car} finished the stage!")
        row, col = new_row, new_col

        break
    elif matrix[new_row][new_col] == 'T':
        kms += 30
        matrix[new_row][new_col] = '.'
        for i in range(size_matrix):
            for s in range(size_matrix):
                if matrix[i][s] == 'T':
                    row,col = i,s
                    matrix[i][s] = '.'
        continue



print(f"Distance covered {kms} km.")

matrix[row][col] = 'C'



for row in matrix:
    print(''.join(row))






