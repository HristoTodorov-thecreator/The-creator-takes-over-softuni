V = int(input())  # area pool in liters
p_one = int(input())  # debit first pipe for hour
p_two = int(input())  # debit second pipe for hour
h = float(input())  # hours for missing worker

total_p_one = p_one * h  # total for first pipe for this hours
total_p_two = p_two * h  # total for second pipe for this hours

two_pipes_total = total_p_two + total_p_one

percentfirstpipe = (total_p_one / two_pipes_total) * 100
percentsecondpipe = (total_p_two / two_pipes_total) * 100

area_pool_percent = (two_pipes_total / V) * 100

liters_overflow = two_pipes_total - V



if area_pool_percent <= 100:
    print(f"The pool is {area_pool_percent:.2f}% full. Pipe 1: {percentfirstpipe:.2f}%. Pipe 2: {percentsecondpipe:.2f}%.")
else:
    print(f"For {h} hours the pool overflows with {liters_overflow:.2f} liters."
)
