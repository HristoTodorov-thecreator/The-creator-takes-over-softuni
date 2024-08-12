player_name = input()

points_that_player_have = 301
totalshots = 0
failedshots = 0
while True:
    sin_dob_or_trip = input()  # single double or triple , retire

    if sin_dob_or_trip == 'Retire':
        print(f"{player_name} retired after {failedshots} unsuccessful shots.")

        break
    points = int(input())
    if sin_dob_or_trip == 'Single' and points <= points_that_player_have:
        points_that_player_have -= points
        totalshots += 1
    elif sin_dob_or_trip == 'Double' and points * 2 <= points_that_player_have:
        points_that_player_have -= points * 2
        totalshots += 1
    elif sin_dob_or_trip == 'Triple' and points * 3 <= points_that_player_have:
        points_that_player_have -= points * 3
        totalshots += 1
    else:
        failedshots += 1
    if points_that_player_have == 0:
        print(f'{player_name} won the leg with {totalshots} shots.')
        break

