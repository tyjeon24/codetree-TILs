dates = list(map(int, input().split()))
start_month, start_day, end_month, end_day = dates
day = input()
last_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

day_map = {"Mon":0,"Tue":1,"Wed":2,"Thu":3,"Fri":4,"Sat":5,"Sun":6}
day = day_map[day]
i = 0
result = 0
while True:
    if i%7==day:
        result += 1
    if start_month == end_month and start_day == end_day:
        break
    i+=1
    start_day += 1
    if last_days[start_month] < start_day:
        start_day = 1
        start_month += 1
print(result)