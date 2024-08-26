result = 10000

arr = list(map(int, input().split()))

for i in range(5):
    for j in range(i, 5):
        for k in range(5):
            first_team = arr[i] + arr[j]
            second_team = arr[k]
            remainder = [idx for idx in range(5) if idx not in [i,j,k]]
            third_team = arr[remainder[0]] + arr[remainder[1]]
            
            team_values = [first_team, second_team, third_team]
            if len(set(team_values)) != 3:
                continue
            else:
                diff = max(team_values) - min(team_values)
                result = min(result, diff)


# 불가능하면 -1 출력
if result == 10000:
    print(-1)
else:
    print(result)