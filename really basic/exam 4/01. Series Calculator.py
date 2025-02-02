from math import floor

name_film = input()
seasons = int(input())
episodes = int(input())
time = float(input())

ad = (time * 0.20)
time_for_episode_with_ad = time + ad

special_episode_time =seasons * 10

total = seasons * episodes * time_for_episode_with_ad + special_episode_time
totalfloor = floor(total)
print(f"Total time needed to watch the {name_film} series is {totalfloor} minutes.")
