import re

locations = input()

pattern = r"(=|/)([A-Z][a-zA-Z]{2,})\1"


match = re.findall(pattern,locations)

valid_destinations = [matc[1].replace('=', '').replace('/', '') for matc in match]

len_ = ''.join(valid_destinations)

g = (', '.join(valid_destinations))
print(f'Destinations: {g}')
print(f'Travel Points: {len(len_)}')

