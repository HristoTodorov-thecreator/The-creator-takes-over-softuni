from sys import maxsize

num_chefs = int(input())
winner = ''
highest_score = - maxsize


for i in range (num_chefs):
    chef_name = input()
    total_points = 0
    while True:
        points = input()
        if points == 'Stop':
            break
        else:
            g = int(points)

        total_points += g
    print(f'{chef_name} has {total_points} points.')

    if total_points > highest_score:
            highest_score = total_points
            winner = chef_name
            print(f'{winner} is the new number 1!')


print(f'{winner} won competition with {highest_score} points!')



