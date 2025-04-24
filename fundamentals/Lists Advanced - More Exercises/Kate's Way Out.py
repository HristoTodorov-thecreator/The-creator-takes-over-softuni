rows = int(input())

maze = [input() for _ in range(rows)]


for r in range(rows):
    if 'k' in maze[r]:
        start_row,start_col = r,maze[r].index('k')
        break


directions = [(-1,0), (1,0),(0,-1),(0,1)]

visited = set()

stack = [(start_row, start_col, 0)]

longest_path = -1


while stack:
    row,col,steps = stack.pop()
    if row < 0 or row >= rows or col < 0 or col >= len(maze[0]):
        longest_path = max(longest_path, steps)
        continue

    if maze[row][col] == '#' or (row, col) in visited:
        continue

    visited.add((row, col))

    for dr, dc in directions:
        stack.append((row + dr, col + dc, steps + 1))

if longest_path > 0:
    print(f"Kate got out in {longest_path} moves")
else:
    print("Kate cannot get out")