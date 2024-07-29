chicken_ = 10.35  # chicken price
fish_ = 12.40  #fish price
vegan_ = 8.15  #vegan price
delivery = 2.50

num_chickens = int(input())
num_fishes = int(input())
num_vegan = int(input())

total_sum = (chicken_ * num_chickens) + (fish_ * num_fishes) + (vegan_ * num_vegan)
dessert_ = total_sum * 0.20  # dessert

pricefor_all = dessert_ + total_sum + delivery  # price for everything
print (pricefor_all)  # printing