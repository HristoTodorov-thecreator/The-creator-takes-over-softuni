sheep_and_wolf = input().split(', ')


counter = 0

for i in sheep_and_wolf[::-1]:


    if counter == 0 and i == 'wolf':
        print(f'Please go away and stop eating my sheep')
    elif i == 'wolf':


         print(f'Oi! Sheep number {counter}! You are about to be eaten by a wolf!')




    counter += 1

