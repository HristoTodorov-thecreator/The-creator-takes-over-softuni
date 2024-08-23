kids = 0
students = 0
standarts = 0
total = 0
totalallsold = 0
while True:
    kids1 = 0
    students2 = 0
    standarts3 = 0



    name_of_the_film = input()
    if name_of_the_film == 'Finish':
        print(f'Total tickets: {totalallsold}')
        print(f"{students / totalallsold * 100:.2f}% student tickets.")
        print(f"{standarts / totalallsold * 100:.2f}% standard tickets.")
        print(f"{kids / totalallsold * 100:.2f}% kids tickets.")
        break

    m = int(input())


    for i in range(m):
        tickets_buy = input()


        if tickets_buy == 'student':
           students2 += 1
           students += 1
           totalallsold += 1
        if tickets_buy == 'kid':
            kids1 += 1
            kids += 1
            totalallsold += 1
        if tickets_buy == 'standard':
            standarts3 += 1
            standarts += 1
            totalallsold += 1



        if tickets_buy == 'End':
            break
    total = kids1 + students2 + standarts3
    print(f'{name_of_the_film} - {total / m * 100:.2f}% full.')