cards = input().split()
count_shuffle = int(input())

for cur_shuf in range(count_shuffle):
    g = len(cards) // 2
    left_part = cards[:g]
    right_part = cards[g:]
    shuffled_deck = []
    for card in range(len(left_part)):
        shuffled_deck.append(left_part[card])
        shuffled_deck.append(right_part[card])
    cards = shuffled_deck

print(cards)