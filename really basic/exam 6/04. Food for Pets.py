days = int(input())
total_food = float(input())

eated_by_dog = 0
eated_by_cat = 0
totalcookie = 0
day = 0
for i in range (days):
    thirddaycook = 0
    thirddaycat = 0

    day += 1
    dog = int(input())
    cat = int(input())
    eated_by_cat += cat
    eated_by_dog += dog
    thirddaycat += cat
    thirddaycook += dog



    if day % 3 == 0:
        cookie = (thirddaycat + thirddaycook)
        totalcookie += cookie * 0.10

total_ = eated_by_dog + eated_by_cat
print(f"Total eaten biscuits: {round(totalcookie)}gr.")
print(f"{total_ / total_food * 100:.2f}% of the food has been eaten.")
print(f"{eated_by_dog / total_ * 100:.2f}% eaten from the dog.")
print(f"{eated_by_cat / total_ * 100:.2f}% eaten from the cat.")


