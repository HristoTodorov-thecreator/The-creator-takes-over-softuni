best_movie = ''

best_sum = -float('inf')
count = 0

while count < 7:
    name_film = input()
    if name_film == 'STOP':
        break

    asci_sum = 0
    length = len(name_film)

    for char in name_film:
        ascii_value = ord(char)
        if 'a' <= char <= 'z':
            asci_sum += ascii_value - 2 * length
        elif 'A' <= char <= 'Z':
            asci_sum += ascii_value - length
        else:
            asci_sum += ascii_value

    if asci_sum > best_sum:
        best_sum = asci_sum
        best_movie = name_film
    count += 1

if count == 7:
    print(f"The limit is reached.")
    print(f"The best movie for you is {best_movie} with {best_sum} ASCII sum.")
else:
    print(f"The best movie for you is {best_movie} with {best_sum} ASCII sum.")
