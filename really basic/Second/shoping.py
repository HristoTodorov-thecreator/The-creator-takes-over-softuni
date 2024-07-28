budget_ = float(input())
number_videocards = int(input())
number_proccesor = int(input())
number_memory = int(input())


videocard_ = 250
proccesor_price = (number_videocards * videocard_ ) * 0.35
momory_price = (number_videocards * videocard_ ) * 0.10

total_video_card_price = videocard_ * number_videocards
total_proccesor_price = proccesor_price * number_proccesor
total_memory_price = number_memory * momory_price

totalsum = total_memory_price + total_proccesor_price + total_video_card_price


if number_videocards > number_proccesor:
    totalsum = totalsum - (totalsum * 0.15)

if budget_ >= totalsum:
    print(f"You have {budget_ - totalsum:.2f} leva left!")
else:
    print(f"Not enough money! You need {totalsum - budget_:.2f} leva more!")