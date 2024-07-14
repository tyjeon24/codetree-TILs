n = int(input())

next_odd_stars = n
next_even_stars = 1

for i in range(n):
    if i%2==0: # 1, 3, 5, ...
        print("* "*next_odd_stars)
        next_odd_stars -= 1
    else:
        print("* "*next_even_stars)
        next_even_stars += 1

for j in range(n):
    if j%2==0: # 1, 3, 5, ...
        print("* "*next_odd_stars)
        next_odd_stars -= 1
    else:
        print("* "*next_even_stars)
        next_even_stars += 1