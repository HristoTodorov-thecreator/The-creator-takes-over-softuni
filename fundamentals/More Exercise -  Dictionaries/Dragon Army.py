number_of_dragons = int(input())
dragons_by_color = {}


for _ in range(number_of_dragons):
    colour, name, damage, health, armor = input().split()
    if colour not in dragons_by_color:
        dragons_by_color[colour] = {}
    dragon_damage = 45 if damage == 'null' else int(damage)
    dragon_health = 250 if health == 'null' else int(health)
    dragon_armor = 10 if armor == 'null' else int(armor)
    dragons_by_color[colour][name] = [dragon_damage, dragon_health, dragon_armor]


averages = {}
for color, dragons in dragons_by_color.items():
    total_damage, total_health, total_armor = 0, 0, 0
    count = len(dragons)
    for stats in dragons.values():
        total_damage += stats[0]
        total_health += stats[1]
        total_armor += stats[2]
    averages[color] = [
        total_damage / count,
        total_health / count,
        total_armor / count
    ]


for color, stats in averages.items():
    print(f"{color}::({stats[0]:.2f}/{stats[1]:.2f}/{stats[2]:.2f})")
    for name, info in sorted(dragons_by_color[color].items()):
        print(f"-{name} -> damage: {info[0]}, health: {info[1]}, armor: {info[2]}")