from math import floor

record_in_seconds = float(input())
distance_in_meters = float(input())
time_in_seconds_for_one_meter = float(input())

seconds  = distance_in_meters * time_in_seconds_for_one_meter
slowing_him = floor(distance_in_meters / 50) * 30

total = slowing_him + seconds

if record_in_seconds <= total:
    print(f"No! He was {total - record_in_seconds:.2f} seconds slower.")

else:
    print(f'Yes! The new record is {total:.2f} seconds.')