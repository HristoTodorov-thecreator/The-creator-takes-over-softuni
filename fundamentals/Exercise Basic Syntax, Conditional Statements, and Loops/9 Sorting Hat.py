

while True:
    names = input()
    if names =='Voldemort':
        print(f'You must not speak of that name!')
        break
    if names == 'Welcome!':
        print(f'Welcome to Hogwarts.')
        break
    g = len(names)
    if g < 5:
        print(f"{names} goes to Gryffindor.")
    elif g ==5 :
        print(f"{names} goes to Slytherin.")
    elif g ==6 :
        print(f"{names} goes to Ravenclaw.")
    elif g > 6:
        print(f"{names} goes to Hufflepuff.")
