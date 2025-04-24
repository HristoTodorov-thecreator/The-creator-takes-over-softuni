number = int(input())
import re

pattern = r'@([A-Za-z]+)[^@\-!:>]*:([0-9]+)[^@\-!:>]*!([AD])![^@\-!:>]*->([0-9]+)'


attacked_planets = []
dest_planets = []


for i in range(number):
    message = input()
    counter = 0

    decrypt = ''
    for t in message:
        if t.lower() in 'star':
            counter += 1
    for s in message:
        g = ord(s)
        next_ = g - counter
        decrypt += chr(next_)

    x = re.finditer(pattern,decrypt)
    if x:
        for o in x:
            planet = o.group(1)
            population = o.group(2)
            type_ = o.group(3)
            soldier = o.group(4)
            for n in planet:
                if n.isdigit():
                    planet = planet.replace(n,'')

            if type_ == 'A':
                attacked_planets.append(planet)
            elif type_ == 'D':
                dest_planets.append(planet)


print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(dest_planets)}")
for planet in sorted(dest_planets):
    print(f"-> {planet}")


