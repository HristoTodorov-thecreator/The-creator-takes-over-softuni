

class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59



    def __init__(self,hours,minutes,seconds):
        self.hours =hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    def get_time(self):
        return f'{self.hours:02}:{self.minutes:02}:{self.seconds:02}'

    def check(self):
        if self.seconds > Time.max_seconds:
            self.minutes += 1
            self.seconds = 0
        if self.minutes > Time.max_minutes:
            self.hours += 1
            self.minutes =0
        if self.hours > Time.max_hours:
            self.hours =0
            self.minutes=0
            self.seconds=0


    def next_second(self):
        self.seconds += 1
        self.check()


        return self.get_time()

time = Time(9, 30, 59)
print(time.next_second())