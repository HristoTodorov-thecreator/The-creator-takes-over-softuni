gradus_ = int(input()) # temperature
time_ = input()  # what time is it


if 10<= gradus_ <=18:
    if time_ == 'Morning':
        print(f"It's {gradus_} degrees, get your {'Sweatshirt'} and {'Sneakers'}.")
    elif time_ == 'Afternoon':
        print(f"It's {gradus_} degrees, get your {'Shirt'} and {'Moccasins'}.")
    elif time_ == 'Evening':
        print(f"It's {gradus_} degrees, get your {'Shirt'} and {'Moccasins'}.")

elif 18 < gradus_ <= 24:
    if time_ == 'Morning':
        print(f"It's {gradus_} degrees, get your {'Shirt'} and {'Moccasins'}.")
    elif time_ == 'Afternoon':
        print(f"It's {gradus_} degrees, get your {'T-Shirt'} and {'Sandals'}.")
    elif time_ == 'Evening':
        print(f"It's {gradus_} degrees, get your {'Shirt'} and {'Moccasins'}.")

elif gradus_ >= 25:
    if time_ == 'Morning':
        print(f"It's {gradus_} degrees, get your {'T-Shirt'} and {'Sandals'}.")
    elif time_ == 'Afternoon':
        print(f"It's {gradus_} degrees, get your {'Swim Suit'} and {'Barefoot'}.")
    elif time_ == 'Evening':
        print(f"It's {gradus_} degrees, get your {'Shirt'} and {'Moccasins'}.")