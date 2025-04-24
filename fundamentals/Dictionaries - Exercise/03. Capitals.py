countries = input().split(', ')
capitals = input().split(', ')


t = dict(zip(countries,capitals))

g = {print(' -> '.join([key,value])) for key,value in t.items()}
