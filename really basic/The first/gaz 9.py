square_meters = float(input())
firstprice = square_meters * 7.61


discount_ = firstprice * 0.18

totalprice_ = firstprice - discount_
print(f"The final price is: {totalprice_} lv.")
print(f"The discount is: {discount_} lv.")