length_ = int(input())
width_ = int(input())
height_ = int(input())
percent = float(input()) / 100

aquarium_ = length_ * width_ * height_
liters_ = aquarium_ / 1000
needed_liters= liters_ * (1-percent)
print(needed_liters)