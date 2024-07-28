from math import ceil
name_film = input()
film_time = int(input())
break_time = int(input())

time_for_eating = break_time / 8
time_relaxation = break_time / 4

timeleft = break_time - time_for_eating - time_relaxation

total = timeleft - film_time

if timeleft >= film_time:
    print(f"You have enough time to watch {name_film} and left with {ceil(timeleft - film_time)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_film}, you need {ceil(abs(film_time - timeleft))} more minutes.")

