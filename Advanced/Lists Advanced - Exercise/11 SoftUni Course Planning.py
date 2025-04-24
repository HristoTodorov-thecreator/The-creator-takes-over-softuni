courses_received = input().split(', ')

while True:
    command = input()
    if command == 'course start':
        break
    g = command.split(':')
    if g[0] == 'Add':
        if g[1] not in courses_received:


            courses_received.append(g[1])
    elif g[0] == 'Insert':
        if g[1] not in courses_received:

            index = g[2]
            courses_received.insert(int(index),g[1])
    elif g[0] == 'Remove':
        if g[1] in courses_received:

            courses_received.remove(g[1])
            exer = f"{g[1]}-Exercise"
            if exer in courses_received:
                courses_received.remove(exer)

    elif g[0] == 'Swap':
        if g[1] in courses_received and g[2] in courses_received:

            first_course = courses_received.index(g[1])
            second_course = courses_received.index(g[2])
            courses_received[first_course],courses_received[second_course] = courses_received[second_course],courses_received[first_course]

            first_exercise = f"{g[1]}-Exercise"
            second_exercise = f"{g[2]}-Exercise"

            if first_exercise in courses_received:
                courses_received.remove(first_exercise)
                courses_received.insert(second_course + 1, first_exercise)

            if second_exercise in courses_received:
                courses_received.remove(second_exercise)
                courses_received.insert(first_course + 1, second_exercise)

    elif g[0] == 'Exercise':
        if g[1] in courses_received:

            exer = f"{g[1]}-Exercise"
            if exer not in courses_received:
                index = courses_received.index(g[1])
                courses_received.insert(index + 1,exer)

        else:
            courses_received.append(g[1])
            courses_received.append(f"{g[1]}-Exercise")

counter = 1
for i in courses_received:

    print(f'{counter}.{i}')
    counter +=1






