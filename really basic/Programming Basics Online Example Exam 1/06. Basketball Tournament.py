
win = 0
loss = 0


while True:
    game = 0
    g = 0
    tournamentname = input()
    if tournamentname == "End of tournaments":
        print(f'{win / (win + loss)* 100:.2f}% matches win')
        print(f'{loss / (win + loss) * 100:.2f}% matches lost')
        break
    numbergames = int(input())
    for i in range (numbergames):
        firstpoints = int(input())
        secondpoints = int(input())
        if firstpoints > secondpoints:
            g = firstpoints - secondpoints
            game += 1
            win += 1
            print(f'Game {game} of tournament {tournamentname}: win with {g} points.')
        else:
            g = secondpoints - firstpoints
            game += 1
            loss += 1
            print(f'Game {game} of tournament {tournamentname}: lost with {g} points.')