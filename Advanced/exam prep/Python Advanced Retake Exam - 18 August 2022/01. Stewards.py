from collections import deque
seq_of_seats = [x for x in input().split(', ')]

first_seqs = deque([int(x) for x in input().split(', ')])
sec_seqs = deque([int(x) for x in input().split(', ')])

seat_matches = []
rotations = 0
while first_seqs and sec_seqs:
    if len(seat_matches) >= 3:
        break

    if rotations >= 10:
        break

    first_num = first_seqs.popleft()
    sec_num = sec_seqs.pop()

    result = first_num + sec_num

    chr_res = chr(result)


    seat_one = str(first_num) + chr_res
    seat_two = str(sec_num) + chr_res



    for seat in [seat_one,seat_two]:


        if seat in seq_of_seats:
            seq_of_seats.remove(seat)
            seat_matches.append(seat)
            break

        elif seat in seat_matches:
            break

        else:
            first_seqs.append(first_num)
            sec_seqs.appendleft(sec_num)

    rotations += 1




print(f'Seat matches: {", ".join(map(str,seat_matches))}')
print(f'Rotations count: {rotations}')


