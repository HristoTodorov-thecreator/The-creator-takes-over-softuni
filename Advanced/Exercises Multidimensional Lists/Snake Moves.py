rows, cols = map(int, input().split())
snake = input()

index = 0
for r in range(rows):
    row = ""
    for c in range(cols):
        row += snake[index]
        index = (index + 1) % len(snake)
    if r % 2 == 1:
        row = row[::-1]
    print(row)