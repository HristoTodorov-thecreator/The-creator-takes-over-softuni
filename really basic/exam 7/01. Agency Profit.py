name_of_company = input()
number_tickets_for_adults = int(input())
number_kids_tickets = int(input())
ticket_cost_for_adults = float(input())
tax = float(input())

ticket_cost_for_kids = ticket_cost_for_adults - (ticket_cost_for_adults * 0.70)
adult_cost_with_tax = ticket_cost_for_adults + tax
ticket_kids_tax = ticket_cost_for_kids + tax

total = number_kids_tickets * ticket_kids_tax + number_tickets_for_adults * adult_cost_with_tax
profit = total * 0.20

print(f"The profit of your agency from {name_of_company} tickets is {profit:.2f} lv.")