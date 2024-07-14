ages = []
while True:
    ages.append(int(input()))
    if ages[-1] >= 30:
        break
print(f"{sum(ages[:-1])/len(ages[:-1]):.2f}")