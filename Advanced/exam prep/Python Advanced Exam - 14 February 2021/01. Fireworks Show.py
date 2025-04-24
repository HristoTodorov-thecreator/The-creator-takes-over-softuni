from collections import deque

fireworks_effects = deque([int(x) for x in input().split(', ')])
explosive_powers = deque([int(x) for x in input().split(', ')])

palm_fireworks = 0
willow_fireworks =0
crossette_fireworks = 0


while fireworks_effects and explosive_powers:
    firework_effect = fireworks_effects.popleft()
    explosive_power = explosive_powers.pop()

    if firework_effect <=0:
        explosive_powers.appendleft(explosive_power)
        continue
    if explosive_power <=0:
        fireworks_effects.appendleft(firework_effect)
        continue


    total = firework_effect + explosive_power

    if total % 5 == 0 and total % 3 == 0:
        crossette_fireworks += 1
    elif total % 3 ==0:
        palm_fireworks += 1
    elif total % 5 == 0:
        willow_fireworks += 1
    else:
        firework_effect -= 1
        fireworks_effects.append(firework_effect)
        explosive_powers.append(explosive_power)



    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >=3:
        print(f'Congrats! You made the perfect firework show!')
        break

else:
    print(f"Sorry. You can't make the perfect firework show.")


if fireworks_effects:
    print(f'Firework Effects left: {", ".join(map(str,fireworks_effects))}')

if explosive_powers:
    print(f'Explosive Power left: {", ".join(map(str,explosive_powers))}')

print(f'Palm Fireworks: {palm_fireworks}')
print(f'Willow Fireworks: {willow_fireworks}')
print(f'Crossette Fireworks: {crossette_fireworks}')



