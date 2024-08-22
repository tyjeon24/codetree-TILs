Y, M, D = map(int, input().split())

def is_leap_year(year):
    result = False
    if year%4==0:
        result = True
        if year%100==0:
            result = False
            if year%400==0:
                result = True
    return result

def get_season(month):
    if 3<=month<=5:
        return "Spring"
    elif 6<=month<=8:
        return "Summer"
    elif 9<=month<=11:
        return "Fall"
    else:
        return "Winter"

last_day = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31,
}

if is_leap_year(Y):
    last_day[2] = 29

if D <= last_day[M]:
    print(get_season(M))
else:
    print(-1)