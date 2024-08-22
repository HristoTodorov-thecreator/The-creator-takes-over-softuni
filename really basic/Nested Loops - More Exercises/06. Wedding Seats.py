last_sector = input()
num_row_first_sector = int(input())
odd_row_places = int(input())


total_places = 0

for sector in range(ord('A'),ord(last_sector) + 1):
    num_rows = num_row_first_sector + (sector - ord('A'))
    for row in range (1,num_rows + 1):
        if row % 2 == 1 :
            num_places = odd_row_places
        else:
            num_places = odd_row_places + 2

        for place in range(97 , 97 + num_places):
            print(f'{chr(sector)}{row}{chr(place)}')
            total_places += 1

print(total_places)