
paintings = list(map(int, input().split()))


while True:
    command = input()
    if command == "END":
        break

    parts = command.split()
    action = parts[0]


    if action == "Change":
        painting_number = int(parts[1])
        new_number = int(parts[2])

        if painting_number in paintings:
            index = paintings.index(painting_number)
            paintings[index] = new_number


    elif action == "Hide":
        painting_number = int(parts[1])

        if painting_number in paintings:
            paintings.remove(painting_number)


    elif action == "Switch":
        painting_number1 = int(parts[1])
        painting_number2 = int(parts[2])

        if painting_number1 in paintings and painting_number2 in paintings:
            index1 = paintings.index(painting_number1)
            index2 = paintings.index(painting_number2)
            paintings[index1], paintings[index2] = paintings[index2], paintings[index1]


    elif action == "Insert":
        index = int(parts[1])
        painting_number = int(parts[2])

        if 0 <= index < len(paintings):
            paintings.insert(index + 1, painting_number)


    elif action == "Reverse":
        paintings.reverse()


print(" ".join(map(str, paintings)))