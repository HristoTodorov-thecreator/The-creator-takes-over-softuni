g = input().split()

row = int(g[0])
col = int(g[1])

matrix = [[int(x) for x in input().split()]for i in range(row)]


maxsum = 0
save = []
for i in range(row-2):

    for x in range(col-2):
        first = matrix[i][x] # Първо
        second = matrix[i+1][x] # Под него
        third = matrix[i][x+1] # до него
        forth = matrix[i+1][x+1] # среда
        fifth = matrix[i+2][x] # доло ляво
        six = matrix[i+2][x+1] # Под среда
        seven = matrix[i+2][x+2] #доло дясно
        eight = matrix[i+1][x+2] #среда дясно
        nine = matrix[i][x+2] #горе дясно

        maxnow = first
        maxnow += second
        maxnow += third
        maxnow += forth
        maxnow += fifth
        maxnow += six
        maxnow += seven
        maxnow +=eight
        maxnow += nine
        if maxnow > maxsum:
            maxsum = maxnow
            if save:
                save.clear()
                save.append(first)
                save.append(third)
                save.append(nine)
                save.append(second)
                save.append(forth)
                save.append(eight)
                save.append(fifth)
                save.append(six)
                save.append(seven)

            else:
                save.append(first)
                save.append(third)
                save.append(nine)
                save.append(second)
                save.append(forth)
                save.append(eight)
                save.append(fifth)
                save.append(six)
                save.append(seven)





print(f'Sum = {maxsum}')

print(' '.join(str(x) for x in save[0:3]))
print(' '.join(str(x) for x in save[3:6]))
print(' '.join(str(x) for x in save[6:9]))






