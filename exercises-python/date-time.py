import datetime

t = datetime.time(5, 25, 1)

print(t)

t.hour
t.minute
t.microsecond

print(datetime.time.min)
print(datetime.time.max)
print(datetime.time.resolution)

today = datetime.date.today()
print(today)

today.timetuple()
today.year
today.month
today.day

