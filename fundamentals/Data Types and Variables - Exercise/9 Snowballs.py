number_of_snowballs_made = int(input())
max_value = 0
max_weight = 0
max_time = 0
max_quality = 0




for i in range(number_of_snowballs_made):
    weight_snowball = int(input())
    time_to_hit_the_target = int(input())
    quality_of_the_snowball = int(input())
    g = (weight_snowball / time_to_hit_the_target) ** quality_of_the_snowball

    if g > max_value:
        max_value = g
        max_weight = weight_snowball
        max_time = time_to_hit_the_target
        max_quality = quality_of_the_snowball

print(f"{max_weight} : {max_time} = {max_value:.0f} ({max_quality})")

