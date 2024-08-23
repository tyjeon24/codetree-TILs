n=int(input())

rain_dates = []

for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        y,m,d = map(int, date.split("-"))
        rain_dates.append((y,m,d,day,weather))

rain_dates = sorted(rain_dates, key=lambda item: (item[0], item[1], item[2]))
print(f"{rain_dates[0][0]}-{int(rain_dates[0][1]):02d}-{int(rain_dates[0][2]):02d} {rain_dates[0][3]} {rain_dates[0][4]}")