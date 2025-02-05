from sys import maxsize

films = int(input())


totalrating = 0
biggestrating = - maxsize
smallest = maxsize
smallestname = ''
biggestname = ''

for i in range(films):
    name_film = input()
    rating = float(input())


    if rating > biggestrating:
        biggestrating = rating
        biggestname = name_film
    if rating < smallest:
        smallest = rating
        smallestname = name_film

    totalrating += rating

print(f"{biggestname} is with highest rating: {biggestrating:.1f}")
print(f"{smallestname} is with lowest rating: {smallest:.1f}")
print(f"Average rating: {totalrating / films:.1f}")

