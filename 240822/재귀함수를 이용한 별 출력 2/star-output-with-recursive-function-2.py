n = int(input())

def print_star(n):
    if n:
        for _ in range(n):
            print("*", end=" ")
        print()
        print_star(n-1)

def print_star_ascending(n, r=0):
    if n!=r:
        for _ in range(r+1):
            print("*", end=" ")
        print()
        print_star_ascending(n, r+1)


print_star(n)
print_star_ascending(n)