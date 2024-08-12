minutes = int(input())
seconds = int(input())
meters = float(input())
seconds_for_making_100_meters = int(input())

totalseconds = minutes * 60 + seconds

timeslowing = meters / 120

totaltimeslowing = timeslowing * 2.5

marintime = (meters / 100) * seconds_for_making_100_meters -totaltimeslowing

if marintime <= totalseconds:
        print(f"Marin Bangiev won an Olympic quota!")
        print(f"His time is {marintime:.3f}.")

else:
        print(f"No, Marin failed! He was {marintime - totalseconds :.3f} second slower.")