cost_for_vegetables_kg = float(input())
cost_for_fruits_kg = float(input())
total_kg_vegetables = int(input())
total_kg_fruits = int(input())

totalvg= cost_for_vegetables_kg * total_kg_vegetables # total vegetables
totalfr = total_kg_fruits * cost_for_fruits_kg # total fruits

totalsumlv = totalvg + totalfr # total lv

total_sum_in_euro = totalsumlv / 1.94  # sum in euro
print(f'{total_sum_in_euro:.2f}') #printing