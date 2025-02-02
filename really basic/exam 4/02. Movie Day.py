

time_for_photos = int(input())
number_scenes = int(input())
time_for_scene = int(input())

preparing = time_for_photos * 0.15
time_for_taking_a_scene = number_scenes * time_for_scene
total = time_for_taking_a_scene + preparing

if time_for_photos >= total:
    print(f"You managed to finish the movie on time! You have {round(time_for_photos - total)} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {round(total - time_for_photos)} minutes.")
