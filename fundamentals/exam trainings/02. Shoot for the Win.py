integers = [int(t) for t in input().split()]
counter = 0
while True:
    command = input()
    if command == 'End':
        break
    index_ = int(command)
    if index_ < len(integers) and integers[index_] != -1:
        counter += 1

        the_value = integers[index_]
        integers[index_] = -1
        for number in range(len(integers)):
            if integers[number] == -1:
                continue

            if integers[number] > the_value:
                integers[number] -= the_value

            else:
                integers[number] += the_value


stri = " ".join(str(n) for n in integers)

print(f'Shot targets: {counter} -> {stri}')