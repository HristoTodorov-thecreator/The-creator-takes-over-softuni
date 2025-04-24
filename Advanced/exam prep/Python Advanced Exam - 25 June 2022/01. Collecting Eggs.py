from collections import deque

seq_numbers_eggs = deque([int(x) for x in input().split(', ')])
seq_numbers_papers = [int(x) for x in input().split(', ')]

filled_boxes = 0

while seq_numbers_eggs and seq_numbers_papers:
    egg = seq_numbers_eggs.popleft()

    if egg <= 0:
        continue

    if egg == 13:

        seq_numbers_papers[0], seq_numbers_papers[-1] = seq_numbers_papers[-1], seq_numbers_papers[0]
        continue

    paper = seq_numbers_papers.pop()

    if egg + paper <= 50:
        filled_boxes += 1


if filled_boxes > 0:
    print(f"Great! You filled {filled_boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if seq_numbers_eggs:
    print(f"Eggs left: {', '.join(map(str, seq_numbers_eggs))}")
if seq_numbers_papers:
    print(f"Pieces of paper left: {', '.join(map(str, seq_numbers_papers))}")