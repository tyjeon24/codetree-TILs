ages = []
while True:
    ages.append(int(input()))
    if ages[-1] >= 30 or ages[-1] < 20:
        break
if len(ages) == 2:
    print(f"{ages[0]:.2f}")
else:
    print(f"{sum(ages[:-1])/len(ages[:-1]):.2f}")