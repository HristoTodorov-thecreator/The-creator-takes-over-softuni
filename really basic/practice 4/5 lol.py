packet_pens = 5.80  # 5.80 per packet
packet_markers = 7.20  # 7.20 per packet
for_cleaning = 1.20  # 1.20 for liter

pens_ = int(input())   #inputs
markers_ = int(input())
cleaning_ = int(input())
discount_ = int(input()) / 100

totalpens_ = pens_ * packet_pens
markers_total = markers_ * packet_markers
cleaning_total = cleaning_ * for_cleaning

total_ = totalpens_ + markers_total + cleaning_total   # total without discount
total_total_ = total_ - (total_ * discount_)  #discount
print(total_total_)  # total with discount