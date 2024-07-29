depsum_ = float(input()) # deposit sum
monthdep_ = int(input()) # monthly deposit
yearpercent_ =float(input()) /100  # we devide with 100 to calculate yearly percent

totalsum_= depsum_ + monthdep_ * ((depsum_* yearpercent_)/12) #formula
print(totalsum_) # printing