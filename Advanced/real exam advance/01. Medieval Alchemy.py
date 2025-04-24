from collections import deque

potions = {
    110: "Brew of Immortality",
    100: "Essence of Resilience",
    90: "Draught of Wisdom",
    80: "Potion of Agility",
    70: "Elixir of Strength"
}
crafted_potions = []




substances = [int(x) for x in input().split(', ')]

levels_crystal_energys = deque([int(x) for x in input().split(', ')])






while substances and levels_crystal_energys:
    substance = substances.pop()
    crystal = levels_crystal_energys.popleft()

    total = substance + crystal

    if total in potions and potions[total] not in crafted_potions:
        crafted_potions.append(potions[total])


    else:
        try_potions = [points for points in potions if points <= total and potions[points] not in crafted_potions]
        if try_potions:
            best_potion = max(try_potions)
            if potions[best_potion] not in crafted_potions:
                crafted_potions.append(potions[best_potion])
                left = crystal - 20
                if left > 0:
                    levels_crystal_energys.append(left)

        else:
            check = crystal - 5

            if check > 0:
                levels_crystal_energys.append(check)


    if len(crafted_potions) == 5:
        break


if len(crafted_potions) == 5:
    print("Success! The alchemist has forged all potions!")
else:
    print("The alchemist failed to complete his quest.")

if crafted_potions:
    print(f"Crafted potions: {', '.join(crafted_potions)}")


if substances:
    print(f"Substances: {', '.join(map(str, reversed(substances)))}")

if levels_crystal_energys:
    print(f"Crystals: {', '.join(map(str, levels_crystal_energys))}")

