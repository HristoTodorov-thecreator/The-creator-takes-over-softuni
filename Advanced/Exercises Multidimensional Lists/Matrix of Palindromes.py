g = input().split()

rows = int(g[0])
cols = int(g[1])
try_ = {  0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j',
  10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't',
  20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

now = []
for i in range(rows):

    for s in range(cols):

        middle = i+s
        if middle > 26:  # Завъртане към началото на азбуката
            middle = (middle - 1) % 26 + 1
        g= f'{try_[i]}{try_[middle]}{try_[i]}'
        now.append(g)

    print(f'{" ".join(now)}')
    now.clear()