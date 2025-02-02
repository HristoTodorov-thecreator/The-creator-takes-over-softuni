
name_film = input()
days = int(input())
tickets = int(input())
price_ticket = float(input())
percent_for_cinema = int(input())

price_for_tickets_a_day = tickets * price_ticket
total_for_all_days = days * price_for_tickets_a_day

makingtopercent = percent_for_cinema / 100
totalall = total_for_all_days - (total_for_all_days * makingtopercent)
print(f'The profit from the movie {name_film} is {totalall:.2f} lv.')