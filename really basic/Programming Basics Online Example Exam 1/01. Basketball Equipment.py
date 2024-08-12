year_tax = int(input())

shoes = year_tax - (year_tax * 0.40)
clothes = shoes - (shoes * 0.20)
ball = clothes / 4
accesories = ball / 5

total_price_with_year_tax = year_tax + shoes + clothes + ball + accesories

print(f"{total_price_with_year_tax:.2f}")