paper = 5.80  # for roll price
cloth = 7.20 # for roll price
glue = 1.20  # for liter price

numberpapers = int(input())
numbercloths = int(input())
glueliters = float(input())
percent_off = int(input())

price_for_the_papers = paper * numberpapers  # price for papers
price_for_cloths = cloth * numbercloths  # price for cloths
price_for_glue = glueliters * glue  # price for glue

total_price = price_for_glue + price_for_cloths + price_for_the_papers

g = percent_off / 100

total_price_with_discount = total_price - (total_price * g)  # total price with discount
print(f'{total_price_with_discount:.3f}')  # print