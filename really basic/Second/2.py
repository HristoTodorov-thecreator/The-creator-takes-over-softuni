points_ = int(input())
total_bonus = 0

if points_ <= 100 :
    total_bonus =  5
elif points_ < 1000 :
    total_bonus = points_ * 0.20
else:
    total_bonus = points_ * 0.10

if points_ % 2 == 0:
        total_bonus = total_bonus + 1
elif points_ % 10 == 5:
        total_bonus = total_bonus + 2


print(total_bonus)
print(points_ + total_bonus)