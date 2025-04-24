element = input().split()

while True:
    command = input()
    if command == '3:1':
        break
    part = command.split()

    if part[0] == 'merge':
        start = int(part[1])
        end = int(part[2])
        if start < 0:
            start = 0
        if end > len(element) - 1:
            end = len(element) - 1
        if start <= end:
            string  = ''.join(element[start:end + 1])
            del element[start:end + 1]
            element.insert(start,string)


    elif part[0] == 'divide':
        first_index = int(part[1])
        partitions = int(part[2])

        if 0 <= first_index < len(element):
            string_to_remake = element[first_index]
            length = len(string_to_remake)

            length_every_part = length // partitions

            result = []
            start = 0

            for m in range(partitions):
                if m < partitions - 1:
                    thepart = string_to_remake[start:start + length_every_part]
                else:
                    thepart = string_to_remake[start:]

                result.append(thepart)
                start += length_every_part

            del element[first_index]
            element[first_index:first_index] = result
print(' '.join(element))





