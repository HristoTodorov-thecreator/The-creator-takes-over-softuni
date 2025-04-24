number_of_heroes = int(input())


heroes = {}

for n in range(number_of_heroes):
    hero = input()
    splitted = hero.split()
    name = splitted[0]
    hp = int(splitted[1])
    mana = int(splitted[2])

    if name not in heroes:
        heroes[name] = {'health':hp,'mana':mana}


while True:
    command = input().split(' - ')
    action = command[0]
    if action == 'End':
        break
    if action == 'CastSpell':
        hero_nam = command[1]
        mp_needed = int(command[2])
        spell_name = command[3]
        if hero_nam in heroes:
            if heroes[hero_nam]['mana'] >= mp_needed:
                heroes[hero_nam]['mana'] -= mp_needed
                pointsnow = heroes[hero_nam]['mana']
                print(f'{hero_nam} has successfully cast {spell_name} and now has {pointsnow} MP!')
            else:
                print(f"{hero_nam} does not have enough MP to cast {spell_name}!")

    if action == 'TakeDamage':
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        if hero_name in heroes:

            heroes[hero_name]['health'] -= damage
            thehp = heroes[hero_name]['health']
            if heroes[hero_name]['health'] > 0:
                print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {thehp} HP left!")

            else:
                print(f"{hero_name} has been killed by {attacker}!")
                del heroes[hero_name]



    if action == 'Recharge':
        hero_na = command[1]
        amount  = int(command[2])
        if hero_na in heroes:
            if heroes[hero_na]['mana'] + amount > 200:
                actual = 200 - heroes[hero_na]['mana']
                heroes[hero_na]['mana'] = 200
                print(f"{hero_na} recharged for {actual} MP!")
            else:
                heroes[hero_na]['mana'] += amount
                print(f"{hero_na} recharged for {amount} MP!")

    if action == 'Heal':
        name = command[1]
        amount = int(command[2])
        if name in heroes:
            if heroes[name]['health'] + amount > 100:
                actual = 100 - heroes[name]['health']
                heroes[name]['health'] = 100
                print(f"{name} healed for {actual} HP!")
            else:
                heroes[name]['health'] += amount
                print(f"{name} healed for {amount} HP!")

for l in heroes:
    hp = heroes[l]['health']
    mana = heroes[l]['mana']
    print(l)
    print(f'  HP: {hp}')
    print(f'  MP: {mana}')
