
numpages_ = int(input())  #  number of pages
hourpages_ = int(input())  #  pages per hour
num_days = int(input())  # number of days

hours_total = numpages_ // hourpages_  # formula 1
hours_a_day = hours_total // num_days  # formula 2

print(hours_a_day)  # printing