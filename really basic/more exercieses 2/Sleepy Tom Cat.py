number_resting_days = int(input())

tom_cat_sleep = 30000  # minutes in year
when_he_is_working = 63  # minutes a day
when_he_is_not_working = 127  #minutes a day

total_minutes_for_not_working = number_resting_days * when_he_is_not_working
working_days = 365 - number_resting_days
minutes_working = working_days * when_he_is_working

play_time = minutes_working + total_minutes_for_not_working

totalplay_time = tom_cat_sleep - play_time

hours = abs(totalplay_time) // 60
minutes = abs(totalplay_time) % 60
if tom_cat_sleep > play_time:

    print('Tom sleeps well')
    print(f"{hours} hours and {minutes} minutes less for play")


else:

    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")