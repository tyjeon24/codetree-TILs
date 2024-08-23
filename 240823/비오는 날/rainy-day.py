n=int(input())

for _ in range(n):
    date, day, weather = input().split()
    if weather == "Rain":
        print(f"{date} {day} {weather}")
        break