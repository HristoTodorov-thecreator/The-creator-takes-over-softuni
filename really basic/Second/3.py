

hours_ = int(input()) #enter number hours
minutes_ = int(input()) # enter number minutes

minutes_ = minutes_ + 15


if minutes_ > 59:
    hours_ = hours_ + 1
    minutes_= minutes_ - 60
if hours_ > 23:
    hours_ = hours_ - 24


print(f'{hours_}:{minutes_:02d}')  # print result



