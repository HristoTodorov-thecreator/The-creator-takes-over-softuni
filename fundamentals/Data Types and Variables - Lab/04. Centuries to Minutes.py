centuries = int(input())

one_year_to_days = 365.2422

total_years = centuries * 100

total_days = int(total_years * one_year_to_days)

total_hours = total_days * 24

total_minutes = total_hours * 60

print(f'{centuries} centuries = {total_years} years = {total_days} days = {total_hours} hours = {total_minutes} minutes')