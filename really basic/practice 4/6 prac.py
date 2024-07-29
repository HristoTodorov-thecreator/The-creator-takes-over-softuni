nylon_ = 1.50  # nylon for square meters
paint_ = 14.50  # paint for liter
thinner_ = 5.00  # thinner for liter
bags_ = 0.40  # for bags


nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_work = int(input())

paint_needed += paint_needed * 0.10


total_mat = thinner_needed * thinner_ + paint_needed * paint_ + ((nylon_needed + 2) *1.50 )  + bags_
payper_hour = total_mat * 0.30   # pay per hour
total_pay = payper_hour * hours_work  # total pay for workers

totalsum_for_all = total_pay + total_mat  #total all
print(totalsum_for_all)  #Printing