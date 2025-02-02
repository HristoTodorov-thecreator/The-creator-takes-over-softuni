name_actor = input()
points_from_academy = float(input())
number_voting_people = int(input())

points = 0
points = points + points_from_academy
for _ in range(number_voting_people):
    name_sec = input()
    g = float(input())
    points = points + (len(name_sec) * g)/2

    if points >= 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points:.1f}!")
        break

else:
     print(f"Sorry, {name_actor} you need {1250.5 - points:.1f} more!")