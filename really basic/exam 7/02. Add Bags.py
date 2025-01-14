Price_baggage = float(input())
kg_baggage = float(input())
days_to_travel = int(input())
number_baggages = int(input())


if kg_baggage < 10:
    Price_baggage = Price_baggage *  0.20
elif 10 <= kg_baggage <=20:
    Price_baggage = Price_baggage / 2

if days_to_travel > 30:
    Price_baggage = Price_baggage + (Price_baggage * 0.10)
elif 7 <= days_to_travel <= 30:
    Price_baggage = Price_baggage + (Price_baggage * 0.15)
elif days_to_travel < 7:
    Price_baggage = Price_baggage + (Price_baggage * 0.40)

Price_baggage = Price_baggage * number_baggages

print(f"The total price of bags is: {Price_baggage:.2f} lv. ")