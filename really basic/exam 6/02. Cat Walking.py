

minutes_for_walking_a_Day = int(input())
number_walks_day = int(input())
calories_taken_from_the_cat = int(input())

total_walking = minutes_for_walking_a_Day * number_walks_day
calories = total_walking * 5


fifty_percent = calories_taken_from_the_cat / 2


if calories >= fifty_percent:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {calories}." )
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {calories}.")