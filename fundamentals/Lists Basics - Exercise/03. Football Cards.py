list_team_a = ['A-1','A-2','A-3','A-4','A-5','A-6','A-7','A-8','A-9','A-10','A-11']
list_team_b = ['B-1','B-2','B-3','B-4','B-5','B-6','B-7','B-8','B-9','B-10','B-11']

counter_a = 11
counter_b = 11




cards = input()
g = cards.split()




for i in g:
    if i in list_team_a :
        list_team_a.remove(i)
        counter_a -= 1
    if i in list_team_b:
        list_team_b.remove(i)
        counter_b -= 1

    if counter_a < 7 or counter_b <7:
        print(f'Team A - {counter_a}; Team B - {counter_b}')
        print(f'Game was terminated')
        break


else:
    print(f'Team A - {counter_a}; Team B - {counter_b}')





