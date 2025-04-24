box_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

racks = 1
current_capacity = rack_capacity

while box_clothes:
    cloth = box_clothes.pop()
    if cloth <= current_capacity:
        current_capacity -= cloth
    else:
        racks += 1
        current_capacity = rack_capacity - cloth

print(racks)