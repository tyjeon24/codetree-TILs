a, b, c = map(int, input().split())

min_value, max_value = min([a,b,c]), max([a,b,c])

for value in [a,b,c]:
    if min_value < value < max_value:
        print(value)