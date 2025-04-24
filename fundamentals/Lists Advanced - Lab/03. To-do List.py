notes = [0] * 10

while True:
    command = input()
    if command == 'End':
        break
    tokens = command.split('-')

    prir = int(tokens[0]) - 1
    note = tokens[1]
    notes.pop(prir)
    notes.insert(prir, note)

result = [elem for elem in notes if elem != 0 ]
print(result)