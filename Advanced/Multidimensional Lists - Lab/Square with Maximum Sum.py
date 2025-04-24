

data = input().split(', ')

rows = int(data[0])
cols = int(data[1])

matrix = []

max_ = -999999999999999999999999
for _ in range(rows):
    data = [int(x) for x in input().split(', ')]
    matrix.append(data)

sub = []

for row in range(len(matrix)-1):

    for col in range(len(matrix[row])-1):
        curr = matrix[row][col]
        next = matrix[row][col + 1]
        el_below = matrix[row + 1][col]
        two_two = matrix[row + 1][col + 1]

        total = curr + next + el_below + two_two

        if total > max_:
            max_ = total
            sub = [[curr,next],[el_below,two_two]]


print(*sub[0])
print(*sub[1])
print(max_)