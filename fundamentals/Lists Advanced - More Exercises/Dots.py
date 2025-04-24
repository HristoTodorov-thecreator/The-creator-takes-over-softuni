def largest(board):
    rows,cols = len(board),len(board[0])
    visited = set()
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(row,col):
        stack = [(row,col)]
        count = 0

        while stack:
            r,c = stack.pop()
            if (r, c) in visited or board[r][c] != ".":
                continue


            visited.add((r,c))
            count += 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if 0 <= nr < rows and 0 <= nc < cols:
                    stack.append((nr, nc))

        return count
    max_group = 0

    for r in range(rows):
        for c in range(cols):
            if (r, c) not in visited and board[r][c] == ".":
                max_group = max(max_group, dfs(r, c))

    return max_group








n = int(input())

board = [input().split() for _ in range(n)]

result = largest(board)

print(result)

