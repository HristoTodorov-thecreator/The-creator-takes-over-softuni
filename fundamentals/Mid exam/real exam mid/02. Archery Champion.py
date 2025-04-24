
targets = list(map(int, input().split("|")))
total_points = 0

while True:
    command = input()
    if command == "Game over":

        break

    if command == "Reverse":
        targets.reverse()


    parts = command.split("@")
    if len(parts) != 3:
        continue



    action = parts[0]
    start_index = int(parts[1])
    length = int(parts[2])


    if action == "Shoot Left":
        if 0 <= start_index < len(targets):

            index = (start_index - length) % len(targets)

            if targets[index] >= 5:
                total_points += 5
                targets[index] -= 5
            else:
                total_points += targets[index]
                targets[index] = 0


    elif action == "Shoot Right":
        if 0 <= start_index < len(targets):

            index = (start_index + length) % len(targets)

            if targets[index] >= 5:
                total_points += 5
                targets[index] -= 5
            else:
                total_points += targets[index]
                targets[index] = 0



print(" - ".join(map(str, targets)))
print(f"John finished the archery tournament with {total_points} points!")