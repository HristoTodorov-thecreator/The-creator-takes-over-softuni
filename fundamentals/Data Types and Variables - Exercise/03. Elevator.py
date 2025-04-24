n_persons = int(input())
capacity_of_persons = int(input())

times_elevated = 0


while n_persons > 0:
    n_persons -= capacity_of_persons
    times_elevated +=1

print(f'{times_elevated}')